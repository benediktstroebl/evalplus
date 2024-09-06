import re
def split_words(txt):
    ans = txt.split(re.compile(r'[ ,]+'))
    if len(ans) == 1:
        if ',' in txt:
            return [txt]
        else:
            return [num_odd_let(txt)]
    else:
        return ans
def num_odd_let(txt):
    return sum(1 for char in txt if ord(char) % 2)