
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

    # input: string
    # output: int

    # input_str = s.upper()
    # sum = 0
    #
    # for char in input_str:
    #     sum += ord(char) - 64
    #
    # return sum

    return sum(ord(c) - 64 for c in s.upper())

