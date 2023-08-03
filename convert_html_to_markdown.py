import os
from bs4 import BeautifulSoup

def replace_html_tags_with_markdown(file_path):
    with open(file_path, 'r') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')

    for h5_tag in soup.find_all('h5'):
        h5_tag.replace_with('##### ' + h5_tag.get_text())

    for h4_tag in soup.find_all('h4'):
        h4_tag.replace_with('#### ' + h4_tag.get_text())

    for h3_tag in soup.find_all('h3'):
        h3_tag.replace_with('### ' + h3_tag.get_text())

    for strong_tag in soup.find_all('strong'):
        strong_tag.replace_with('**' + strong_tag.get_text() + '**')

    for em_tag in soup.find_all('em'):
        em_tag.replace_with(em_tag.get_text())

    for code_tag in soup.find_all('code'):
        code_tag.replace_with('`' + code_tag.get_text() + '`')

    for kbd_tag in soup.find_all('kbd'):
        kbd_tag.replace_with('`' + kbd_tag.get_text() + '`')

    for aside_tag in soup.find_all('aside'):
        aside_tag.replace_with(aside_tag.get_text())

    for pyprez_tag in soup.find_all('pyprez-editor'):
        pyprez_tag.replace_with('```python\n' + pyprez_tag.get_text() + '\n```')

    for a_tag in soup.find_all('a'):
        if a_tag.has_attr('href'):
            link_text = a_tag.get_text()
            link_url = a_tag['href']
            a_tag.replace_with(f"[{link_text}]({link_url})")
    
    for img_tag in soup.find_all('img'):
        img_src = img_tag.get('src', '')
        img_alt = img_tag.get('alt', '')
        img_title = img_tag.get('title', '')
        if img_tag.has_attr('title'):
            img_tag.replace_with(f"![{img_alt}]({img_src} \"{img_title}\")")
        else:
            img_tag.replace_with(f"![{img_alt}]({img_src})")

    for ul_tag in soup.find_all('ul'):
        for li_tag in ul_tag.find_all('li'):
            li_tag.replace_with('- ' + li_tag.get_text())
        ul_tag.replace_with(ul_tag.get_text())

    for ol_tag in soup.find_all('ol'):
        count = 1
        for li_tag in ol_tag.find_all('li'):
            li_tag.replace_with(f"{count}. {li_tag.get_text()}")
            count += 1
        ol_tag.replace_with(ol_tag.get_text())

    for tag in soup.find_all():
        if tag.name == 'div' and 'alert' in tag.get('class', []):
            if 'alert-secondary' in tag.get('class', []):
                tag.replace_with(':::important\n' + tag.get_text(strip=True) + '\n:::')
            elif 'alert-info' in tag.get('class', []):
                tag.replace_with(':::note\n' + tag.get_text(strip=True) + '\n:::')
            elif 'alert-warning' in tag.get('class', []):
                tag.replace_with(':::warning\n' + tag.get_text(strip=True) + '\n:::')

    updated_md_content = str(soup)

    with open(file_path, 'w') as file:
        file.write(updated_md_content)

def process_directory(directory_path):
    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                replace_html_tags_with_markdown(file_path)

# directory_path = input("Directory path:")
directory_path = "/Users/lewis.baker/Desktop/markdown-files"
process_directory(directory_path)
