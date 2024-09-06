
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
    txt = txt.lower()
    txt = txt.replace(" ", "")
    txt = txt.replace(",", " ")
    txt = txt.split(" ")
    txt = [word.lower() for word in txt]
    if txt:
        return txt[0], txt[1:]
    else:
        count = 0
        for letter in "abcdefghijklmnopqrstuvwxyz":
            if len(letter) % 2 == 1:
                count += 1
        return count, []
