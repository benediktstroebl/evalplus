def split_words(txt):
    whitespace_exists = ' ' in txt
    comma_exists = ',' in txt
    if whitespace_exists:
        return txt.split()
    elif comma_exists:
        return txt.split(',')
    else:
        odd_lowercase = len(list(filter(lambda c: c.islower(), txt))) % 2 == 0
        if odd_lowercase:
            return [True]
        else: 
            return [False]