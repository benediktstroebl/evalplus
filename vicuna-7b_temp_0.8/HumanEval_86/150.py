
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
    # Create a list of characters and store the length of the string
    char_list = [ord(c) for c in s]
    string_len = len(s)
    # Shuffle the characters
    random.shuffle(char_list)
    # Reverse the string by adding the length of the string to the end of each character
    return ''.join(chr(i) for i in char_list) + string_len
