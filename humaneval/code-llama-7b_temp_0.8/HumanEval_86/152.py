
def anti_shuffle(s):
    """
    Write a function that takes a string and returns an ordered version of it.
    Ordered version of string, is a string where all words (separated by space)
    are replaced by a new word where all the characters arranged in
    ascending order based on ascii value.
    Note: You should keep the order of words and blank spaces in the sentence.

    For example:
    anti_shuffle('Hi') returns 'Hi'
    anti_shuffle('hello') returns 'ehllo'
    anti_shuffle('Hello World!!!') returns 'Hello !!!Wdlor'
    """
    # initialize a blank string
    new_string = ""
    # split the sentence on the basis of spaces
    words = s.split()
    for word in words:
        # initialize a blank string
        new_word = ""
        # split the word on the basis of letters
        letters = word.split()
        # loop through each letter
        for letter in letters:
            new_letter = ""
            # loop through each letter in the word
            for i in range(len(letter)):
                # check if the letter is alphabet
                if ord(letter[i]) >= 65 and ord(letter[i]) <= 90:
                    # add it to new letter
                    new_letter += chr(ord(letter[i]) - 65)
                elif ord(letter[i]) >= 97 and ord(letter[i]) <= 122:
                    # add it to new letter
                    new_letter += chr(ord(letter[i]) - 97)
                else:
                    # add it to new letter
                    new_letter += letter[i]
            # add the new letter to the new word
            new_word += new_letter
        # add the word to the final string
        new_string += new_word + " "
    # remove the last extra space
    return new_string[:-1]
