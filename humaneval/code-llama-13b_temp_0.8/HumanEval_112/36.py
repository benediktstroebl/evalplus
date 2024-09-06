
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
    # first make list from string s
    s_list = list(s)
    # second check if any letters in string c is in s
    for i in c:
        if i in s_list:
            # if it is, delete it from s_list
            s_list.remove(i)
    # third make string from list
    new_s = ''.join(s_list)
    # fourth make reverse from string
    new_s_reversed = new_s[::-1]
    # fifth check if both strings are palindrome
    if new_s == new_s_reversed:
        # if it is palindrome, return tuple with both string and True
        return (new_s,True)
    else:
        # if it is not palindrome, return tuple with both string and False
        return (new_s,False)
