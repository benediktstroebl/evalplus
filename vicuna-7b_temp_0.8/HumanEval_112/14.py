
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
    result = ""
    for i in range(len(s)):
        if i+1 == len(s):
            # if current character is the last character in the string
            if s[i] == s[i+1]:
                # if the current character is repeated
                if s[i] in s[0:i]:
                    # then replace the current character with an empty string
                    result = result + " "
                else:
                    # if the current character is not repeated
                    result = result + s[i]
        else:
            # if current character is not the last character in the string
            result = result + s[i]
    return (result, True) if result == s[::-1] else (result, False)