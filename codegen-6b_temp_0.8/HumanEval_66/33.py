
def digitSum(s):
    """Task
    Write a function that takes a string as input and returns the sum of the upper characters only'
    ASCII codes.

    Examples:
        digitSum("") => 0
        digitSum("abAB") => 131
        digitSum("abcCd") => 67
        digitSum("helloE") => 69
        digitSum("woArBld") => 131
        digitSum("aAaaaXa") => 153
    """
    res = 0
    for i in range(len(s)):
        if 97 <= ord(s[i]) <= 122:
            res += ord(s[i])-91
        else:
            res += ord(s[i])
    return res

