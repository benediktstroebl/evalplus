
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
    if not txt.isspace():
        if not txt.replace(",", "").isspace():
            return txt.split(',')
        else:
            count_lower_case_letters = 0
            for i in txt.lower():
                if ord(i) % 2 == 0 and 97 <= ord(i) <= 122:
                    count_lower_case_letters += 1
            return count_lower_case_letters
    else:
        return None
