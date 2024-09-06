import re
def split_words(txt):
    spaced = re.findall(r'\w+|[,\s]', txt)
    if len(spaced) == 1 and ',' not in txt:
        return len(txt.lower()) - sum(1 for c in txt if c != ' ')
    return spaced