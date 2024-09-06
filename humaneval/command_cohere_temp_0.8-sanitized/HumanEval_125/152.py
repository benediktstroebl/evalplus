import re
def split_words(txt):
    ans = txt.split(re.compile(r'[ ,]+'))
    if len(ans) == 1:
        if ',' in txt:
            return [txt]
        else:
            return [str(len(set(txt)) - (txt.isalpha() and txt.lower() == txt))];
    else:
        return ans