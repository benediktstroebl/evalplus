
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
    # Iterate through the string
    for char in s:
        # If the character is not a letter, append it to the result string
        if ord(char) > 32:
            result += char
        else:
            # If the character is a letter, convert it to its uppercase
            # form and append it to the result string
            result += char.upper()
    return result