
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
    # s = input()
    # c = input()
    # reverse_s = s[::-1]
    reverse_s = ''
    for i in s:
        if i not in c:
            reverse_s += i
    reverse_s = reverse_s[::-1]
    print(reverse_s)
    if reverse_s == s:
        return ('',True)
    else:
        return (reverse_s,False)
