import re
def split_words(txt):
    if re.findall(r'\s', txt): 
        return txt.split(' ')
    elif re.findall(r',', txt): 
        return txt.split(',')
    else:
        return len(list(filter(lambda c: ord(c) % 2 == 0, txt.lower())))