
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

    def isUpper(char):
        if 'A' <= char <= 'Z':
            return True
        return False

    total = 0
    for char in s:
        if isUpper(char):
            total += ord(char)

    return total

