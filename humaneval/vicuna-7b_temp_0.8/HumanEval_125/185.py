
def split_words(txt):
    '''
    Given a string of words, return a list of words split on whitespace, if no whitespaces exists in the text you
    should split on commas ',' if no commas exists you should return the number of lower-case letters with odd order in the
    alphabet, ord('a') = 0, ord('b') = 1, ... ord('z') = 25
    Examples
    split_words("Hello world!") ➞ ["Hello", "world!"]
    split_words("Hello,world!") ➞ ["Hello", "world!"]
    split_words("abcdef") == 3 
    '''
    txt = txt.strip()
    if not txt:
        return 0
    elif txt.endswith(','):
        return txt[:-1].split(',')
    elif ',' not in txt:
        return len(txt.split(''))
    else:
        txt = txt.lower()
        odd_ord = [ord(c) if ord(c) % 2 == 1 else 0 for c in txt]
        return [c for c in txt if c in 'abcdefghijklmnopqrstuvwxyz' and ord(c) not in odd_ord]
