
def reverse_delete(s,c):
    """Task
    We are given two strings s and c, you have to deleted all the characters in s that are equal to any character in c
    then check if the result string is palindrome.
    A string is called palindrome if it reads the same backward as forward.
    You should return a tuple containing the result string and True/False for the check.
    Example
    For s = "abcde", c = "ae", the result should be ('bcd',False)
    For s = "abcdef", c = "b"  the result should be ('acdef',False)
    For s = "abcdedcba", c = "ab", the result should be ('cdedc',True)
    """
    # use list comprehension
    # example:
    # my_list = [x for x in range(10)]
    # print(my_list)
    # >>> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    #
    # my_list2 = [x for x in range(10) if x % 2 == 0]
    # print(my_list2)
    # >>> [0, 2, 4, 6, 8]
    #
    # my_list3 = [x for x in range(10) if x % 2 == 0 if x > 5]
    # print(my_list3)
    # >>> [6, 8]
    new_string = ''.join([x for x in s if x not in c])
    is_palindrome = (new_string == new_string[::-1])
    return (new_string, is_palindrome)
