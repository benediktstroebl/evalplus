
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
    # Use a set to store the characters in order, and add new characters to it
    # as you encounter them in the input string
    characters = set()
    for char in s:
        characters.add(ord(char))
    # Create a string of the same length as the input string, but with all
    # the characters in the correct order
    result = ''.join(sorted(reversed(characters)))
    return result
