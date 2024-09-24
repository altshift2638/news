import requests
from bs4 import BeautifulSoup

# List of cybersecurity news sources
news_sources = [
    "https://cybersecurityventures.com/today"
    "https://thehackernews.com"
    "https://www.cyberscoop.com",
    "https://www.threatpost.com",
    "https://www.securityweek.com",
    "https://www.darkreading.com"
]

# Function to scrape news articles
def scrape_news():
    articles = []
    for source in news_sources:
        try:
            response = requests.get(source)
            soup = BeautifulSoup(response.text, 'html.parser')

            # Example of finding headlines (this may vary by site)
            for headline in soup.find_all('h2'):  # Adjust the tag and class as needed
                title = headline.get_text()
                link = headline.find('a')['href']
                articles.append({'title': title, 'link': link})

        except Exception as e:
            print(f"Error accessing {source}: {e}")

    return articles

# Function to filter for new threats
def filter_threats(articles):
    threats = []
    for article in articles:
        if "threat" in article['title'].lower() or "vunrability" in article['title'].lower() or"attack" in article['title'].lower():
            threats.append(article)
    return threats

if __name__ == "__main__":
    print("Scanning for new cyber threats...")
    all_articles = scrape_news()
    new_threats = filter_threats(all_articles)

    if new_threats:
        print("New cyber threats found:")
        for threat in new_threats:
            print(f"- {threat['title']}: {threat['link']}")
    else:
        print("No new threats found.")