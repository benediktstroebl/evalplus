
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
    # 1) if there are spaces, split on spaces and return
    # 2) if there are no spaces, split on commas and return
    # 3) if neither, then return the number of lower-case letters with odd order in the alphabet

    if ' ' in txt:
        return txt.split()
    elif ',' in txt:
        return txt.split(',')
    else:
        alphabet_list = list(txt)
        odd_letters = []
        for letter in alphabet_list:
            if ord(letter)%2 != 0:
                odd_letters.append(letter)
        return len(odd_letters)
