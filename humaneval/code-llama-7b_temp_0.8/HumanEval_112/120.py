
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
    # get the list of characters in c
    c_list = list(c)
    c_list.sort()
    # create a list of all characters in s
    s_list = list(s)
    # check if the characters in s are all in the list of c
    for char in s_list:
        if char in c_list:
            # if the character is in the list, delete it
            s_list.remove(char)
    # join the list back into a string
    s_list = "".join(s_list)
    # check if the list is a palindrome
    if s_list == s_list[::-1]:
        return s_list, True
    else:
        return s_list, False

