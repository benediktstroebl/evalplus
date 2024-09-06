
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
    return sum([ord(c) for c in s.upper() if ord(c) > 47 and ord(c) < 58])

    # return sum(ord(c) for c in s if c.isupper())

    # return sum(ord(c) for c in s if c >= 'A' and c <= 'Z')

    # return sum(ord(c) for c in s if c in string.ascii_uppercase)
