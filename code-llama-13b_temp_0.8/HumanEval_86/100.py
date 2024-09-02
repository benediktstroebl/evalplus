
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
    if len(s) == 0:
        return ''
    s_list = s.split()
    ordered_list = []
    for item in s_list:
        item_list = list(item)
        item_list.sort()
        item_list = "".join(item_list)
        ordered_list.append(item_list)
    return " ".join(ordered_list)

