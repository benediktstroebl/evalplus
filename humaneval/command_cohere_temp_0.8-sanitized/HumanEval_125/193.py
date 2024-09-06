import re
def split_words(txt):
    ans = re.findall(r'\w+|[^,\s]\S*',' '.join(txt.split()).replace(',', ' '))
    if not ans:
        ans = len([x for x in txt if x.islower() and ord(x) % 2 == 0])
    return ans