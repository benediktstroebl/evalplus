
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
    # lambda solution
    # return sum(map(lambda c: ord(c)-96 if c.isupper() else 0, s))
    # print(ord('A'))
    return sum(ord(c) - 96 if c.isupper() else 0 for c in s)

    #
    # return sum([ord(c) - 96 if c.isupper() else 0 for c in s])

