
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
    s = s.lower()
    new_string = ""
    for word in s.split():
        new_char = ""
        for char in word:
            if char.isdigit():
                new_char += char
            else:
                new_char += chr(ord(char) + 1)
        new_string += new_char
    return new_string