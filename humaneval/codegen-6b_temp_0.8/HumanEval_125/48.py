
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
    ascii_lowercase = []
    for i in range(ord('a'), ord('z') + 1):
        ascii_lowercase.append(chr(i))
    split_array = [word for word in txt.split()]
    for word in split_array:
        if word.isalpha():
            if ord(word[0]) % 2 == 1:
                return split_array
            else:
                continue
        else:
            continue
    return len(ascii_lowercase)

