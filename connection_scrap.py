from bs4 import BeautifulSoup
import json
import re

def scrape_html_page(file_path):
    pattern = re.compile(r"\s+")
    
    with open(file_path, "r", encoding="unicode_escape") as f:
        html_content = f.read()

    soup = BeautifulSoup(html_content, "html.parser")
    span_elements = soup.find_all("span", class_="class_name")
    
    names = []
    for span_element in span_elements:
        name = re.sub(pattern, " ", span_element.text).strip()
        names.append(name)

    print(len(names))
    
    with open("output.json", "w") as f:
        json.dump(names, f)

if __name__ == "__main__":
    file_path = "file.html"
    scrape_html_page(file_path)
