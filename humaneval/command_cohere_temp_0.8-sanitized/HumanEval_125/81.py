import re
def split_words(txt):
    ans = []
    txt = re.sub(r',', ' ', txt)
    ans = txt.split()
    if not ans: ans = len(re.findall(r'[a-z]', txt))
    return ans