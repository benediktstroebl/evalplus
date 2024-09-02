
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
    # s = "abAB"
    # s = "abcCd"
    # s = "helloE"
    # s = "woArBld"
    # s = "aAaaaXa"
    string = s.upper()
    # print(string)

    intSum = 0
    for i in string:
        # print(ord(i))
        intSum += ord(i)

    return intSum

