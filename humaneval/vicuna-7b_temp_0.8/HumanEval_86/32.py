
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
    if not s:
        return ''
    else:
        new_string = ''
        for char in s:
            if char.isalnum() and char not in '':
                new_string += char
            elif char == ' ':
                new_string += ''.join(sorted(s.split()))
            else:
                new_string += char
        return new_string
