import re
def split_words(txt):
    ans = txt.split(re.escape(r'[ ,]+'))
    if len(ans) == 1:
        ans = re.findall(r'\b\w+\b', txt)
        if len(ans) == 1:
            return len(txt.lower())
        else:
            return len(ans)
    else:
        return ans