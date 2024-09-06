import re
def split_words(txt):
    ans = txt.split(re.compile(r'[ ,]+'))
    if not ans:
        ans = len(txt)
    return ans