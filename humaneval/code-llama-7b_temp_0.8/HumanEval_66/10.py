
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
    # # Your code here
    # sum = 0
    # for i in range(len(s)):
    #     if ord(s[i]) >= 65 and ord(s[i]) <= 90:
    #         sum += ord(s[i])
    # return sum
    # or
    return sum(ord(i) for i in s if 65 <= ord(i) <= 90)

