
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
    # 1st brute-force solution
    # total = 0
    # for char in s:
    #     if char.isupper():
    #         total += ord(char)

    # 2nd solution - convert to int and sum ASCII codes
    # sum_total = 0
    # for char in s:
    #     sum_total += ord(char)
    # return sum_total

    # 3rd solution - sum ASCII codes
    return sum([ord(char) for char in s if char.isupper()])

