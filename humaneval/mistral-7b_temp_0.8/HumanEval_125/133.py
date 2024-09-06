
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
    try:
        split_string = txt.split()
        if len(split_string) == 0:
            split_string = txt.split(',')
        if len(split_string) == 0:
            number_of_odd_letter = 0
            for letter in txt:
                number_of_odd_letter += 1 if ord(letter) % 2 == 0 else 0
            return number_of_odd_letter
        else:
            return split_string
    except Exception:
        return "error"
