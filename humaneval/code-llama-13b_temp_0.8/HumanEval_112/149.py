
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
    # should return a tuple
    # return [result, bool]
    if s == "":
        return ["", True]
    # if no string to delete
    elif len(c) == 0:
        return [s, True]
    # if a char is equal to a char in c
    elif c[0] in s:
        s = s.replace(c[0], "")
        return [s, True]
    # else
    else:
        return [s, False]

    # print(reverse_delete("abcde", "ae"))
    # print(reverse_delete("abcdef", "b"))
    # print(reverse_delete("abcdedcba", "ab"))
    # print(reverse_delete("sesame", "az"))
    # print(reverse_delete("", ""))
    # print(reverse_delete("", "a"))
    # print(reverse_delete("abcdedcba", ""))

