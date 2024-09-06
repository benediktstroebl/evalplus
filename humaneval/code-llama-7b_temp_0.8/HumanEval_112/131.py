
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
    # ANALYSIS
    # 1. Create a table for reverse s.
    # 2. For each character in reverse s, find out whether it is in c. If it is, skip it.
    # 3. Add the rest to the result string.
    # 4. Check if the result string is palindrome.
    # 5. Return result string and palindrome boolean.
    result = ''
    reverse_s = s[::-1]
    for i in range(len(reverse_s)):
        if reverse_s[i] in c:
            continue
        result += reverse_s[i]
    return (result, result == result[::-1])
