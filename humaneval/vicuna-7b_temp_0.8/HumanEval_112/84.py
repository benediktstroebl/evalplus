
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
    s_length = len(s)
    c_length = len(c)

    # Check if the two strings are not empty
    if s_length == 0 or c_length == 0:
        return '', False

    result_string = ""
    reverse_list = list(range(s_length))
    for i in range(0, s_length-1, 1):
        reverse_list[i] = reverse_list[i] + 1
        result_string = result_string + str(reverse_list[i])
    for i in range(1, c_length):
        if c[i-1] in result_string:
            result_string = result_string[:i] + str(i) + result_string[i+1:]
            reverse_list[i] -= 1
            if reverse_list[i] < 0:
                reverse_list[i] = 0
        else:
            reverse_list[i] += 1

    return result_string, True