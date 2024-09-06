def split_words(txt):
    ans = txt.split(',') if ',' in txt else txt.split() if ' ' in txt else len([x for x in txt if x.isalpha() and x.lower() not in 'abcdefghijklmnopqrstuvwxyz'])
    return ans