
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

    str_list = s.split()
    new_string = ""
    for i in range(len(str_list)):
        str_list[i] = sorted(str_list[i])
    for str in str_list:
        new_string += ''.join(str) +''
    new_string = new_string[:-1] # remove the last space
    return new_string
