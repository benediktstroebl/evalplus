import re
def split_words(txt):
    spaced = txt.split(',')
    if len(spaced) > 1:
        return spaced
    spaced = re.findall(r'\w+', txt)
    if len(spaced) > 1:
        return spaced
    return len(txt)