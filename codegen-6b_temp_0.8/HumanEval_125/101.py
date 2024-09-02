
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
    lst = []
    count = 0
    if not len(txt):
        return None
    if not isinstance(txt, str) or not all(isinstance(n, str) for n in txt):
        return None
    if txt == txt.lower() and txt != '':
        text = txt
    else:
        text = txt.lower()
    for character in text:
        if character == ',' or character == ' ':
            if count % 2 == 0:
                lst.append(text[:count])
                text = text[count:]
            else:
                lst.append(text[:count])
                text = text[count:]
            if not text:
                return lst
            count = 0
        else:
            count += 1
    if count % 2 == 0:
        lst.append(text[:count])
    else:
        lst.append(text[:count])
    return lst
    
    