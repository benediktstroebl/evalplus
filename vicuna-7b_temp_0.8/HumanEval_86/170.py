
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
    # Simple implementation of the problem
    # Convert string to list of characters
    string_to_list = list(string)
    # Sort the list based on ASCII value
    string_to_list.sort(key=lambda x: ord(x))
    # Convert the list back to a string
    result = ''.join(string_to_list)
    return result