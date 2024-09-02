
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

    lst = s.split()
    new_lst = []
    for i in range(len(lst)):
        new_lst.append('')

    for i in range(len(lst)):
        for j in range(len(lst[i])):
            new_lst[i] = new_lst[i] + chr(ord(lst[i][j]))

    return''.join(new_lst)

