
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
    print(s)
    str_list = s.split()
    print(str_list)
    print(len(str_list))
    print("----------------------------------------------------------------------")
    for index in range(len(str_list)):
        str_list[index] = ''.join(sorted(str_list[index]))
    print(str_list)
    s = " "
    s = s.join(str_list)
    print(s)
    return s
