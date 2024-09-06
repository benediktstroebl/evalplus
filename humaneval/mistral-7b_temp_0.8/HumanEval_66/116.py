
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
    s = s.upper()
    s = list(s)
    res = 0
    for i in s:
        if i.isalpha():
            res += ord(i) - 64
        else:
            res += ord(i)
    return res

