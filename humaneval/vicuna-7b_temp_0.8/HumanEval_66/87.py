
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
    s = ''.join(sorted(s))
    result = 0
    length = len(s)
    for i in range(1, length):
        result = result + (s[0] - ord(s[i])) * 10 ** (length - i - 1)
    return result
