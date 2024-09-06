
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
    if not s or s == ' ' or s.isdigit():
        return s

    s_list = s.split()
    new_s_list = []
    for i in s_list:
        new_string = ''.join(sorted(i))
        new_s_list.append(new_string)
    return ' '.join(new_s_list)

