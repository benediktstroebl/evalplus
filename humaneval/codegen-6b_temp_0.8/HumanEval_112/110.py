
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
    c_idx = list()
    for i in range(len(c)):
        if c[i] not in s:
            continue
        c_idx.append(i)
    if len(c_idx) == 0:
        return '', False
    else:
        result = ''
        i = 0
        j = len(c_idx) - 1
        while i < len(s):
            if j >= 0:
                if s[i] == c[c_idx[j]]:
                    result += s[i]
                    i += 1
                    j -= 1
                else:
                    result += s[i]
                    i += 1
            else:
                result += s[i]
                i += 1
        # print(result)
        if result == result[::-1]:
            return result, True
        else:
            return result, False
