
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
    # set of string to track
    t = set()
    # input to track
    i = txt
    # initialise counter
    count = 0
    # loop through the string
    for c in i:
        # punc is either a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, v, w, x, y, z
        if c in "abcdefghijklmnopqrstuvwxyz":
            # check if the current character is in the string
            if c not in t:
                # add to the string
                t.add(c)
            else:
                # string has duplicates so current character should not be added to string
                # print("Current character is already in string")
                pass

        # punc is either a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, v, w, x, y, z
        if c in "abcdefghijklmnopqrstuvwxyz":
            # check if the current character is in the string
            if c not in t:
                # add to the string
                t.add(c)
            else:
                # string has duplicates so current character should not be added to string
                # print("Current character is already in string")
                pass
            # character is in the string so we should add it to the count
            count += 1
            # print(t)
    return count

