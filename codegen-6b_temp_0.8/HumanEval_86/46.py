
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
    words = s.split(' ')
    ascii_list = []
    for word in words:
        ascii_list.append(ord(word[0]))
    sorted_list = sorted(ascii_list)
    return_str = ''
    for index, i in enumerate(sorted_list):
        return_str += words[index][0]
    return return_str
