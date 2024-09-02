
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

    # Python has a built-in function called split() that does exactly that.
    # The built-in split() function takes a string and splits it based on a separator(the whitespace by default).
    # The separator is not included in the resulting list.
    if ',' in txt:
        # Splits on a comma
        return txt.split(',')
    elif ' ' in txt:
        # Splits on a space
        return txt.split()
    else:
        # No space or comma, split on the alphabet's order
        letters = []
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        for i in range(26):
            letters.append(alphabet[i])
        #print(letters)
        odd_letters = []
        for i in range(len(letters)):
            if i % 2 == 1:
                odd_letters.append(letters[i])
        #print(odd_letters)
        return len(odd_letters)
