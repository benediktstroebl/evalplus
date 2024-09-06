
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
    # String reversal
    rev_str = ""
    for i in range(len(s)-1,-1,-1):
        rev_str += s[i]

    res = []
    for i in s:
        if i not in c:
            res.append(i)

    res_str = "".join(res)

    # Palindrome check
    palindrome_check = True
    if res_str != rev_str:
        palindrome_check = False

    return (res_str, palindrome_check)

