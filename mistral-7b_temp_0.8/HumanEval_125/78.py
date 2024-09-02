
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
    # Solution 1
    # txt = txt.split()
    # return txt

    # Solution 2
    # count = 0
    # for x in txt:
    #     if ord(x) % 2 != 0:
    #         count += 1
    # return count

    # Solution 3
    # return [txt] if txt == txt.replace(" ", "").replace(",", "") else txt.split()

    # Solution 4
    # if txt.find(" ") == -1:
    #     return txt.split(",")
    # else:
    #     return txt.split()

    # Solution 5
    # return txt.split() if txt.find(" ") != -1 else txt.split(",")

    # Solution 6
    # return (
    #     txt.replace(" ", "").replace(",", "").split(",")
    #     if txt.find(" ") == -1
    #     else txt.split()
    # )

    # Solution 7
    # return (
    #     txt.replace(" ", "
