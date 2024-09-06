
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
    #create a new string with all the characters in c
    c_set = set(c)
    new_c = ''.join(sorted(c_set))
    result = ''
    #reverse the string
    for char in s:
        result += char
    # check if the reversed string is equal to the original string
    if s == result[::-1]:
        return result, True
    else:
        return result, False
