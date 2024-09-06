import re
def split_words(txt):
    lst = re.findall(r'\w+', txt)
    if len(lst) > 0:
        return lst
    else:
        commas = txt.count(',')
        if commas > 0:
            return txt.split(',')
        else:
            return len(txt.lower())%2==0