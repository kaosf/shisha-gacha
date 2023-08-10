import json
import random

def load_flavors(flavors_file):
    with open(flavors_file, encoding = "utf-8") as file:
        flovors_list = json.load(file)
    fl = []
    for flavor_list in flovors_list:
        fl.append(flavor_list["name"])
    return fl


def load_tags(tags_file):
    with open(tags_file, encoding = "utf-8") as file:
        tag_list = json.load(file)
    tag = []
    for tag_dict in tag_list:
        tag.extend(tag_dict["tag"])
    return tag


def load_blocklist(block_file):
    with open(block_file, encoding = "utf-8") as file:
        blocklist = json.load(file)
    return blocklist
block = load_blocklist('/content/shisha_date/blocklist.json')


def check_exclution(tag, blocklist):
    for flavor_tag in tag:
        if flavor_tag in blocklist:
            if set(tag) and set(blocklist[flavor_tag]):
                return True
    return False

flavors = load_flavors('/content/shisha_date/shisha_info.json')
tag = load_tags('/content/shisha_date/shisha_info.json')
blocklist = load_blocklist('/content/shisha_date/blocklist.json')


num_draw = 4
unipue_results = set()

while len(unipue_results) < num_draw:
    selected_flavor = random.sample(flavors,3)
    selected_flavor.sort()

    if not check_exclution(selected_flavor, blocklist):
        unipue_results.add(tuple(selected_flavor))

for result in unipue_results:
    print(list(result))
