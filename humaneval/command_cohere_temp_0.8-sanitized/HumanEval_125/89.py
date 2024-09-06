import re
def split_words(txt):
    splits = txt.split(',') if re.search(r'\W', txt) == None else txt.split()
    return splits if splits != [None] else len(min(txt.lower(), key=lambda x: (x.count('z'), x.count('a'))))