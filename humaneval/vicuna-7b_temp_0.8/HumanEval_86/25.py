
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
    # Your code here
    # Here's one way to do it:
    ordered_string = ""
    for char in s:
        if char.isalpha():
            # Get the ascii value of the character
            ascii_value = chr(ord(char) + 32)
            # Append the ascii value to the ordered_string
            ordered_string += ascii_value
        else:
            # Append the original character to the ordered_string
            ordered_string += char
    return ordered_string