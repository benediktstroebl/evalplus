
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
    s_list = s.split()
    result_list = [x for x in s_list if x != c[0]]
    reverse_string = "".join(result_list)
    if len(reverse_string) == len(reversed(reverse_string)):
        return (reverse_string, True)
    else:
        return (reverse_string, False)
