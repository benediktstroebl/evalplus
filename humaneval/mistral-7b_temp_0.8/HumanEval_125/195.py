
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
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    if alphabet.count(txt.lower()) == 1:
        return [txt.lower()]
    elif txt.count(" ") == 1:
        txt_split = txt.split()
        return txt_split
    elif txt.count(",") == 1:
        txt_split = txt.split(",")
        return txt_split
    else:
        o_count = 0
        for letter in txt.lower():
            if letter in alphabet:
                if o_count == 0 and letter == "a":
                    o_count += 1
                    continue
                if letter == alphabet[o_count - 1]:
                    o_count += 1
                else:
                    o_count = 0
        return o_count



