
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
    # Create a list of all the characters in the string
    alphabet = set(string.ascii_uppercase)
    word = ''
    # Iterate through the string
    for char in s:
        # Add the character to the current word if it's in the alphabet
        if char in alphabet:
            word += char
        # If the word is not empty, add it to the output string
        if word:
            returnword = ""
            for i in range(len(word)):
                # Add the next character from the word to the current character in the output string
                returnword += word[i] + alphabet.pop(alphabet.index(word[i]))
            # Add a space to separate words
            returnword += " "
            # If the word is not empty, add it to the output string
            returnword += word[i]
            # Add a space to separate words
            returnword += " "
            # If the word is not empty, add it to the output string
            returnword += word[i]
            # Add a space to separate words
            returnword += " "
            # If the word is not empty, add it to the output string
            returnword += word[i]
    # If the word is empty, return an empty string
    return ""
