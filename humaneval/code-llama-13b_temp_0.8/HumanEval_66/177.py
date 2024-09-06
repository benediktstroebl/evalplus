
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
    if s == "":
        return 0
    elif len(s) == 1:
        if s.isupper():
            return ord(s)
        else:
            return 0
    elif s[0].isupper():
        return ord(s[0]) + digitSum(s[1:])
    else:
        return digitSum(s[1:])

