
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
    
    # the most efficient code in terms of runtime complexity is O(n) and also in space complexity
    # Runtime: 76 ms, faster than 63.72% of Python3 online submissions for Reverse Delete to Win.
    # Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Reverse Delete to Win.
    
    temp = ''
    for i in s:
        if i not in c:
            temp += i
    return temp, temp[::-1]==temp

    # the worst code in terms of runtime complexity is O(n^2) and also in space complexity
    # Runtime: 208 ms, faster than 42.11% of Python3 online submissions for Reverse Delete to Win.
    # Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Reverse Delete to Win.
    
    temp = ''
    for i in s:
        if i not in c:
            temp += i
    return temp, temp[::-1] in temp
