
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
    if not s:
        return 0
    else:
        digitSum = 0
        s_chars = set(s)
        for char in s_chars:
            digitSum = digitSum + ord(char)
        return digitSum
