import feedparser
# 可用 openai/baidu/deepl API 优化翻译
FEEDS = {
    'AI': [
        'https://www.technologyreview.com/feed/',
        'https://www.theverge.com/rss/index.xml'
    ],
    # 可补其它类目的RSS
}

def translate(text, target_lang='zh'):
    # 这里只做演示，推荐集成机器翻译API
    return text

def get_top_news(max_news=20):
    news_items = []
    for category, feeds in FEEDS.items():
        for url in feeds:
            fp = feedparser.parse(url)
            for entry in fp.entries[:5]:
                title_en = entry.title
                title_zh = translate(entry.title, 'zh')
                summary = entry.summary[:80] if hasattr(entry, 'summary') else ''
                source = entry.get('source', category)
                link = entry.link
                news_items.append({
                    'category': category,
                    'title_en': title_en,
                    'title_zh': title_zh,
                    'summary': summary,
                    'source': source,
                    'url': link
                })
    # 可加自定义排序
    result = []
    for idx, news in enumerate(news_items[:max_news]):
        item_fmt = (
            f"{idx+1}.【类目】{news['category']}\n"
            f"【标题】{news['title_en']}（{news['title_zh']}）\n"
            f"【内容提要】{news['summary']}\n"
            f"【信息源】{news['source']}\n"
            f"【原文链接】{news['url']}\n"
        )
        result.append(item_fmt)
    return result
