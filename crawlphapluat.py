from bs4 import BeautifulSoup
import requests
import json

def crawl_and_save(url, output_file):
    # Lấy nội dung HTML từ URL
    response = requests.get(url)
    html_content = response.text

    # Parse HTML bằng BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Tìm và lấy nội dung trong thẻ có class là 'content1'
    content_div = soup.find('div', class_='content1')
    if content_div:
        # Tìm tất cả các thẻ <p> trong content_div (loại bỏ các thẻ <p> ở phần đầu tiên)
        paragraphs = content_div.find_all('p')[2:]  # Bỏ qua 2 thẻ <p> đầu tiên

        # Tạo list chứa các mục luật có chapter_name bắt đầu bằng "Điều"
        laws = []

        for paragraph in paragraphs:
            if paragraph.find('b'):  # Nếu có thẻ <b>, đó là tiêu đề của mục luật
                chapter_name = paragraph.text.strip()
                if chapter_name.startswith("Điều"):
                    current_law = {
                        'chapter_name': chapter_name,
                        'content': ''
                    }
                    laws.append(current_law)
            elif laws:  # Nếu không phải thẻ <b>, thêm vào nội dung mục luật cuối cùng
                laws[-1]['content'] += paragraph.text.strip() + '\n'

        # Lưu vào file JSON
        with open(output_file, 'w', encoding='utf-8') as file:
            json.dump(laws, file, ensure_ascii=False, indent=4)
    else:
        print(f"Không tìm thấy nội dung trong {url}")

# URL của từng luật và file output tương ứng
urls = [
    ('https://thuvienphapluat.vn/van-ban/Bo-may-hanh-chinh/Luat-Dan-quan-tu-ve-2019-366794.aspx', 'law1.json'),
    ('https://thuvienphapluat.vn/van-ban/Lao-dong-Tien-luong/Bo-Luat-lao-dong-2019-333670.aspx', 'law2.json'),
    ('https://thuvienphapluat.vn/van-ban/Linh-vuc-khac/Luat-nghia-vu-quan-su-2015-282383.aspx', 'law3.json')
]

# Lặp qua từng URL để crawl và lưu
for url, output_file in urls:
    crawl_and_save(url, output_file)
