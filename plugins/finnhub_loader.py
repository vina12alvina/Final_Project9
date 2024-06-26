import finnhub


def scrape_news():
    finnhub_client = finnhub.Client(api_key="cpr734hr01qifjjvjr0gcpr734hr01qifjjvjr10")

    news = finnhub_client.general_news('general', min_id=0)

    return news
