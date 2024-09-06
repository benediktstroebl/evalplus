
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
    # Use a map to store the mapped characters and their new ascii value
    map_char = {64: 97, 97: 65, 65: 98, 98: 66, 66: 99, 99: 79, 79: 100, 100: 89}
    new_string = ''
    for char in s:
        new_char = ''.join([chr(map_char[ord(char)]) for ord(char) in map(lambda x: x if x > 96 else x-26, s)])
        new_string += char + new_char
    return new_string
