
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
    #
    # if ' ' in txt:
    #     return txt.split()
    # elif ',' in txt:
    #     return txt.split(',')
    # else:
    #     odd_letter_count = 0
    #     for i in txt:
    #         if ord(i) % 2 == 0:
    #             odd_letter_count += 1
    #     return odd_letter_count
    #
    #
    #
    #
    # # if ' ' in txt:
    # #     return txt.split()
    # # elif ',' in txt:
    # #     return txt.split(',')
    # # else:
    # #     return len([i for i in txt if ord(i)%2])
    #
    #
    #
    # #
    # #
    # #
    #
    # if ' ' in txt:
    #     return txt.split()
    # elif ',' in txt:
    #     return txt.split(',')
    # else:
    #     count = 0
    #     for i in txt:
    #         if i.lower() == i and ord(i) % 2 == 1:
    #             count += 1
    #     return count
    #
    # if ' ' in txt:
    #     return txt.split()
    # elif ',' in txt:
    #     return txt.split(',')
    # else:
    #     return len([i for i in txt if ord(i)%2])
    #
    #
    #
    # if ' ' in txt:
    #     return txt.split()
    # elif ',' in txt:
    #     return txt.split(',')
    # else:
    #     return len([i for i in txt if ord(i)%2])
    #
    #
    #
    #
    # if ' ' in txt:
    #     return txt.split()
    # elif ',' in txt:
    #     return txt.split(',')
    # else:
    #     return len([i for i in txt if ord(i)%2
