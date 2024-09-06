
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
    # implement your solution here
    result = txt.lower().split()
    print(result)
    if len(result) == 1:
        number = 0
        for char in result[0]:
            if ord(char) % 2 == 1:
                number += 1
        return number
    else:
        return len(result)


assert split_words("abcdef") == 3
assert split_words("Hello world!") == ["Hello", "world!"]
assert split_words(",,,,,,,,") == 3
assert split_words("!") == 1


