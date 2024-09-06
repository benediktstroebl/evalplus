
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

    if len(s) == 0:
        return 0

    if len(s) == 1:
        return ord(s[0])

    if len(s) == 2:
        return ord(s[0]) + ord(s[1])

    return ord(s[0]) + digitSum(s[1:])

    # first = ord(s[0])
    # rest = digitSum(s[1:])
    # return first + rest

