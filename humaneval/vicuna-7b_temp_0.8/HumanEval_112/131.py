
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
    if len(s) == 0:
        return '', True
    d = set(c)
    s = s.translate(str.maketrans("", "", string.punctuation))
    for char in s:
        d.remove(char)
    result = ""
    for char in s:
        if char in d:
            continue
        result += char
    if s == result[::-1]:
        return result, True
    return result, False
