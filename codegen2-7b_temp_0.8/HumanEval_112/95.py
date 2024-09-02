
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
    counts = [0]*128
    for i in s:
        counts[ord(i)] += 1
    counts[ord(c)] -= 1
    if counts.count(0)!= len(s):
        return (s, False)
    else:
        if (sum([i>0 for i in counts])%2 == 1) and s[0]!= c:
            return (s[1:] + s[:-1], True)
        elif (sum([i>0 for i in counts])%2 == 0) and s[0] == c:
            return (s[1:], True)
        else:
            return (s,
