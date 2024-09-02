
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
    # solution 1
    if not s:
        return 0
    # solution 2
    # return sum(map(ord, filter(str.isupper, s)))
    # solution 3
    return sum(c.isupper() and ord(c) - 64 for c in s)
