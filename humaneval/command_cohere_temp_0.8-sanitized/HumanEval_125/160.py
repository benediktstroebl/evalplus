import re
def split_words(txt):
    ans = txt.split(re.escape(r'[ ,]+'))
    if len(ans) > 0:
        return ans
    else:
        return len(re.findall(r'[a-z]', txt)) % 2