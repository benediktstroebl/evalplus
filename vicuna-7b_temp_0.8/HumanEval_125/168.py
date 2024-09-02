
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
    # If txt is empty return an empty list
    if not txt:
        return []
    
    # Split the txt into a list of words
    words = txt.split()
    
    # If there are no whitespaces in the txt, split on commas
    if not words:
        words = txt.split(',')
    
    # If there are still no whitespaces or commas, return the number of lower-case letters with odd order in the alphabet
    if not words:
        words = txt.lower().split()
        odd_letters_index = [ord(letter) - 1 for letter in words]
        return len(set(odd_letters_index)) & 1
    
    return words
