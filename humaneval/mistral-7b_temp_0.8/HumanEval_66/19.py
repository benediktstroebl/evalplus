
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
    i=0
    digit = 0
    if s == '':
        return digit
    for i in range(len(s)):
        if ord(s[i]) >= 65 and ord(s[i]) <= 90:
            digit += ord(s[i])
    return digit
