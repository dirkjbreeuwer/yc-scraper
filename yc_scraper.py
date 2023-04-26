import requests
import re

batches = ['S21', 'W21', 'S22', 'W22', 'S23']

# Define headers to mimic a browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
    'Referer': 'https://www.ycombinator.com',
    'Accept-Language': 'en-US,en;q=0.9'
}

for batch in batches:
    page = 1
    while True:
        response = requests.get(f'https://api.ycombinator.com/v0.1/companies?batch={batch}&page={page}', headers=headers)
        page_data = response.json()

        print(f"Batch {batch} Page {page_data['page'] + 1} of {page_data['totalPages']}")

        for company in page_data['companies']:
            try:
                html = requests.get(company['website'], headers=headers)
                html_text = html.text
                githubs = re.findall(r'github.com\/[-A-Za-z0-9_./]+', html_text)
                print(f"{company['name']}, {company['website']}, {company['url']}, [{'|'.join(githubs)}]")
            except Exception as e:
                print(f"{company['name']}, {company['website']} #SITEDOWN, {company['url']}, []")

        if page_data['nextPage'] is None:
            break
        else:
            page += 1
