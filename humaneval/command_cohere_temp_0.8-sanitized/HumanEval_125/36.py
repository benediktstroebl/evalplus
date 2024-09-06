import re
def split_words(txt):
    if re.search(r'\s', txt): 
        return txt.split()
    elif re.search(r',', txt): 
        return txt.split(',')
    else: 
        return len(list(filter(lambda x: ord(x) % 2 == 0, txt)))