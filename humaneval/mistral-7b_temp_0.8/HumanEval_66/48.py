
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
    # Write your code here
    #    sum = 0
    #    for char in s:
    #        if char.isupper() == True:
    #            sum = sum + ord(char)
    #    return sum

    # for char in s:
    #     if char.isupper():
    #         sum = sum + ord(char)
    # return sum

    # sum = 0
    # for char in s:
    #     if char.isupper():
    #         sum = sum + ord(char)
    # return sum

    return sum(ord(char) for char in s if char.isupper())

