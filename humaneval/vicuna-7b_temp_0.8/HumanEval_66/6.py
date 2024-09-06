
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
    if s == '':
        return 0
    else:
        n = len(s)
        d = 0
        for i in range(n-1, 0, -1):
            d = d + (ord(s[i]) - ord(s[i-1])) if ord(s[i]) > ord(s[i-1]) else d
        return d