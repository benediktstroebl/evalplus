
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
    return sum(ord(x) for x in s.upper() if ord(x) >= 65 and ord(x) <= 90)

    # while True:
    #     try:
    #         val = ord(s.upper())
    #         if val >= 65 and val <= 90:
    #             sum += val
    #     except IndexError:
    #         break

    # return sum

