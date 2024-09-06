
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
    if len(s)==0:
        return 0
    if s[0].isalpha():
        return  digitSum(s[1:]) + (ord(s[0]) - ord('a') + 1)
    else:
        return digitSum(s[1:])
