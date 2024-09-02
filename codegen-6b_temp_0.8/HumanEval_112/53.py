
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
    
    """ This is a solution without using any builtin string method, very brute force
    """
    def to_list(s):
        return list(s)
    
    def to_string(l):
        return ''.join(l)
    
    s = to_string(s)
    c = to_string(c)
    
    ans = []
    for i in range(len(s)):
        if s[i] in c:
            ans.append(s[i])
    
    reverse_s = to_list(s)[::-1]
    
    ans.extend(reverse_s)
    
    s_revert = to_string(ans)
    
    if s_revert == s_revert[::-1]:
        return (str(s_revert),True)
    else:
        return (str(s_revert),False)

