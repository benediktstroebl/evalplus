
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
    digit_sum = 0
    for i in range(len(s)):
        digit_sum += ord(s[i]) - ord('0')
    return digit_sum

s = input("Enter a string: ")
result = digitSum(s)
