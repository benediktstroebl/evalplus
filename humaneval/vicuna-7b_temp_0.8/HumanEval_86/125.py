
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
    # Use a list to store the characters of each word
    word_chars = [ord(c) for c in s]
    # Reverse the list
    word_chars.reverse()
    # Use a string to store the new words
    result = ''
    # Loop through the list
    for i in range(0, len(word_chars), 1):
        # Get the first character
        char = word_chars[i]
        # Add it to the result
        result += chr(char)
        # Add a space
        result += ' '
    return result

s = input()
