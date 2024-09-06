
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
    txt = txt.lower()
    txt = txt.split()
    txt = txt.translate(str.maketrans("", "", string.punctuation))
    txt = txt.split(',') if ',' in txt else txt.split()
    txt = [x.strip() for x in txt]
    txt = [x for x in txt if len(x) > 2]
    txt = [x for x in txt if all(ord(x) not in '0123456789')]
    txt = txt[::-1]
    txt = txt.reverse()
    txt = txt[::-1]
    txt = [x for x in txt if x not in txt]
    txt = [x for x in txt if x.isalpha()]
    txt = [x for x in txt if x.isdigit()]
    txt = txt[::-1]
    txt = txt[::-1]
    txt = txt.reverse()
    txt = txt.split()
    txt = txt.translate(str.maketrans("", "", string.punctuation))
    txt = txt.split(',') if ',' in txt else txt.split()
    txt = [x.strip() for x in txt]
    txt = [x for x in txt if len(x) > 2]
    txt = [x for x in txt if all(ord(x) not in '0123456789')]
    txt = txt[::-1]
    txt = txt.reverse()
    txt = txt[::-1]
    txt = txt.split()
    txt = txt.translate(str.maketrans("", "", string.punctuation))
    txt = txt.split(',') if ',' in txt else txt.split()
    txt = [x.strip() for x in txt]
    txt = [x for x in txt if len(x) > 2]
    txt = [x for x in txt if all(ord(x) not in '0123456789')]
    txt = txt[::-1]
    txt = txt.reverse()
    txt = txt
