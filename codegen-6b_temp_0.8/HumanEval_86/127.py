
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
    # split the string
    s_list = s.split()
    # sort the list
    s_list.sort()
    # join the list
    s_list = ' '.join(s_list)
    return s_list

assert(anti_shuffle('Hi') == 'Hi')
assert(anti_shuffle('hello') == 'ehllo')
assert(anti_shuffle('Hello World!!!') == 'Hello !!!Wdlor')

