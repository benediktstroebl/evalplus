
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

    # break s into words
    # for each word, make a list of characters in ascending order
    # put the list back into s

    # not the most efficient way
    lst = s.split()
    for i in range(len(lst)):
        lst[i] = ''.join(sorted(lst[i]))
    return ' '.join(lst)
