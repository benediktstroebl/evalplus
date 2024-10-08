
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
    sum = 0
    for char in s:
        if 64 < ord(char) < 91 or 96 < ord(char) < 123:
            sum += ord(char)
    return sum
