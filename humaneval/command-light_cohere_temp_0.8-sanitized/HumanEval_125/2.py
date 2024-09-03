import re
def split_words(txt):
    return [w for w in re.findall('\\s+|\.,|-]', txt)]