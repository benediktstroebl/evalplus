
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
    #Write your code here
    wordlist = []
    wordlist.append(txt)
    if (txt.count(' ') != 0):
        words = txt.split()
        wordlist.append(words)
    elif (txt.count(',') != 0):
        words = txt.split(',')
        wordlist.append(words)
    elif (txt.count(':') != 0):
        words = txt.split(':')
        wordlist.append(words)
    else:
        wordlist.append(len([c for c in txt if ord(c) < ord('z')]))
    return wordlist

