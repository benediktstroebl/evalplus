
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

    # check if c is in s
    if c in s:
        # create a new list to store the values
        lst = list(s)
        # iterate over the list and check if the value is in c
        for i in lst:
            if i in c:
                # if it is then delete it from the list
                lst.remove(i)
        # return the new list as a string and the check
        return "".join(lst), "".join(lst) == "".join(lst[::-1])
    else:
        # if the c is not in s then return s and the check
        return s, s == s[::-1]
