
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
    s = s.upper()  # convert string to uppercase
    if len(s) == 0:
        return 0
    result = 0
    for i in range(len(s)):
        result = result + ord(s[i])
    return result
