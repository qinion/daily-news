from news_crawler import get_top_news
from mailer import send_mail

if __name__ == '__main__':
    news_list = get_top_news()
    if not news_list:
        print("No news to send.")
        exit(0)
    content = "\n\n".join([str(n) for n in news_list])
    send_mail(
        to_addr="619488300@qq.com",
        subject="每日科技新闻日报",
        content=content
    )
print(f"news_list has {len(news_list)} items")
