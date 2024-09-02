
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
    # Here we will use a string builder to build the new string
    # Instead of using the split method which will return a list
    # and then converting it to a string and then joining it
    # This way we can build the new string directly
    new_string = ""
    # Iterating over the characters of the original string
    for char in s:
        # If the char is a space, append the original char to the new_string
        if char == " ":
            new_string += char
        # If the char is not a space, append the new_string to the new_string
        # and add the char to the new_string
        else:
            new_string += char
    return new_string