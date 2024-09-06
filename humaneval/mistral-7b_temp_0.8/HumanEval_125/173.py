
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
    # list of 26 elements
    words_list = []
    # set the string to lowercase
    txt = txt.lower()
    # for each character in the text
    for letter in txt:
        # if the letter is a word character (space)
        if letter.isspace():
            # add the character to the list
            words_list.append(letter)
        # if the character is not a word character
        else:
            # if the character is a comma
            if letter == ',':
                # add the character to the list
                words_list.append(letter)
            # if the character is a lowercase letter
            elif letter.islower():
                # check the ordinal value of the character
                # if the ordinal value is odd
                if ord(letter) % 2 == 1:
                    # add the character to the list
                    words_list.append(letter)
    # return the list of words
    return words_list
