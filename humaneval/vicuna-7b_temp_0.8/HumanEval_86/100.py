
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
    # TODO: Write code to solve the problem
    # You can use a dictionary to store the ASCII values of each letter
    # Then, iterate through the string and replace each letter with its corresponding value
    # in the dictionary.
    # Keep track of the original position of each letter as you go.
    # At the end, return a new string with the letters in the correct order.

    # Example implementation
    s = s.lower()
    result = ''
    for i, c in enumerate(s):
        result += chr(ord(c) - 65)
    return result