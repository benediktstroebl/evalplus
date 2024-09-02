
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
    d={char:0 for char in c}
    for char in s:
        if char in d:
            d[char]+=1
    result=""
    for char in s:
        if char in d:
            if d[char] > 0:
                d[char]-=1
            else:
                result+=char
    if result == result[::-1]:
        return (result,True)
    return (result,False)
