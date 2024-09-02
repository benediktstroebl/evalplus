
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
    left,right = 0,len(s) -1
    while left <= right:
        while left <= right and s[left] != c[right % len(c)]:
            left += 1

        while left <= right and s[right] != c[right % len(c)]:
            right -= 1

        if left <= right:
            s = s[:left] + s[right] + s[left+1:right] + s[left] + s[right+1:]
            left,right = 0,len(s) -1

    if s == s[::-1]:
        return (s, True)
    else:
        return (s, False)



