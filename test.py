import json
from bs4 import BeautifulSoup

with open("result.json", "r") as in_file:
    result_json = json.load(in_file)
    for blog_entry in result_json:
        parsed_html = BeautifulSoup(blog_entry["content"], "html.parser")
        parsed_text = "".join(parsed_html.get_text().split())
        # Print the last 30 chars of every blog
        print(parsed_text[-30:])
