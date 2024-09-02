
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
    if not s:
        return ("",True)

    # if the string is empty
    if len(s) == 1:
        return (s,True)

    # if the string has only one character
    if len(s) == 2:
        if s[0] == s[1]:
            return ("",True)
        else:
            return (s,False)

    # if the string has more than one character
    lst = list(s)
    final_result = ""
    for i in range(len(lst)):
        if lst[i] in c:
            del lst[i]
    for i in range(len(lst)):
        final_result += lst[i]

    if final_result == "":
        return ("",True)
    if final_result[::-1] == final_result:
        return (final_result,True)
    return (final_result,False)
