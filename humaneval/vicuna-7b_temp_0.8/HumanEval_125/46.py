
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
    if re.search('\w', txt):
        return txt.split()
    else:
        num = sum([ord(letter) for letter in txt]) // 2
        if num % 2 == 0:
            return [chr(num)]
        else:
            return [chr(num-1), chr(num+1)]
