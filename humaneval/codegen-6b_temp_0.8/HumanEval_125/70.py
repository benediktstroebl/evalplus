
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
    word_count = 0
    if len(txt) == 0:
        return []

    if txt[0].isalpha() is True:
        word_count += 1
        
    last_letter = chr(ord(txt[0]) - ord('a') + 1)

    for letter in txt[1:]:
        if letter.isalpha() and letter > last_letter:
            word_count += 1
            last_letter = chr(ord(letter) - ord('a') + 1)
        elif letter.isalpha() and letter < last_letter:
            last_letter = chr(ord(letter) - ord('a') + 1)
        elif letter.isalpha():
            continue
        elif letter.isdigit():
            continue
        else:
            return word_count
    return word_count
