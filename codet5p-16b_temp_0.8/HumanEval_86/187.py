
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

    s_list = s.split()
    ordered_s_list = []
    while s_list:
        curr_word = s_list.pop(0)
        curr_word_list = list(curr_word)
        curr_word_list.sort()
        ordered_s_list.append(''.join(curr_word_list))
    return''.join(ordered_s_list)
