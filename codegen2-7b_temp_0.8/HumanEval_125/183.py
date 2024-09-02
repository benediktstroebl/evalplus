
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
    word_list = txt.split()
    word_list_comma = txt.split(',')
    word_list_digit = [letter for letter in txt if letter.isalpha() and ord(letter) % 2 == 0]
    word_list_uppercase = [letter for letter in txt if letter.isalpha() and ord(letter) % 2!= 0]
    if not word_list_comma:
        return len(word_list)
    else:
        return word_list_comma
    
