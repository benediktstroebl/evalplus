
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

    s = list(s)
    for idx, i in enumerate(s):
        s[idx] = ord(i)
        if s[idx] < 65 or s[idx] > 90:
            s[idx] = 0
    return sum(s)

    # another variant
    # s = list(s)
    # return sum([ord(i) for i in s if ord(i) in range(65, 91)])

