
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

    s = s.upper()
    print(s)
    # digitSum = 0
    # for i in s:
    #     if i.isdigit():
    #         digitSum = digitSum + int(i)
    #     elif i.isupper():
    #         digitSum = digitSum + ord(i)
    #
    # return digitSum
    return sum(ord(i) if i.isupper() else int(i) for i in s)
