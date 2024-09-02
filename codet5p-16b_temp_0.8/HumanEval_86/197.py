
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

    new_string = ''
    current_string = ''
    # capitalize the first letter of every word
    for c in s:
        if c.isalpha():
            current_string += c.upper()
        else:
            current_string += c

    new_string += current_string[0]

    for index in range(1, len(current_string)):
        if current_string[index]!= current_string[index - 1]:
            new_string += current_string[index]
    return new_string

