
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
    shuffle_list = s.split(' ')
    new_list = []
    for i in shuffle_list:
        if len(i) == 0:
            new_list.append(i)
        else:
            new_list.append(''.join(sorted(i)))
    return ' '.join(new_list)
