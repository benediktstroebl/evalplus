import re
def split_words(txt):
    ans = txt.split(re.escape(r'[ ,]+'))
    if len(ans) == 1:
        if ',' in txt:
            return [txt]
        else:
            return [num_odd_chars(txt)]
    else:
        return ans
def num_odd_chars(txt):
    return sum(1 for char in txt if ord(char) % 2)