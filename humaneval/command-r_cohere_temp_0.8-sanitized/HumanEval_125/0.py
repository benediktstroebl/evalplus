def split_words(txt):
    '''
    Splits the input string on different delimiters and returns the resulting words as a list. 
    The priority of the delimiters is as follows: space, comma ','. 
    If no such characters exist in the input, returns the number of lower-case letters with odd order in the alphabet.
    '''
    # split on spaces
    words = txt.split()
    if words:
        return words
    
    # split on commas
    words = txt.split(',')
    if words:
        return words
    
    # count odd ordered lower-case letters
    return sum(1 for c in txt if c.lower() and ord(c) % 2 == 1)