
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

    # 1. split string into a list of words
    # 2. sort the list
    # 3. re-create a string out of sorted list

    # s_list = s.split()

    # # return " ".join(sorted(s_list))

    # def anti_shuffle_lister(s_list):
    #     # 1. split string into a list of words
    #     # 2. sort the list
    #     # 3. re-create a string out of sorted list
    #     return " ".join(sorted(s_list))
    # return anti_shuffle_lister(s_list)

    return " ".join(sorted(s.split()))

