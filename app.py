from flask import Flask, render_template, request
import requests
import pandas as pd

API_KEY = 'YOUR_API_KEY'
CSE_ID = 'YOUR_CSE_ID'

app = Flask(__name__)

def google_search(api_key, cse_id, domain, start=1): # start: Control the index of the first result to return
    base_url = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'key': api_key, 
        'cx': cse_id, 
        'q': f'site:{domain}',
        'start': start
        }
    response = requests.get(base_url, params=params)
    return response.json()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/export', methods=['POST'])
# Function to return search results per request
def export():
    domain = request.form['domain']
    search_results = []

    for i in range(1, 100, 10):
        results = google_search(
            api_key=API_KEY,
            cse_id=CSE_ID,
            domain=domain,
            start=i)
        
        items = results.get('items', [])
        if not items:
            break

        search_results.extend(items)

    # Convert results to two keys
    formatted_results = [
        {'URL': item['link'], 'Page Title': item['title']} for item in search_results
    ]
    df = pd.json_normalize(formatted_results)
    df.to_csv('google_search_results.csv', index=False)
        
    return f"CSV file created for {domain}, {len(df)} results found."

if __name__ == '__main__':
    app.run(debug=True)
    