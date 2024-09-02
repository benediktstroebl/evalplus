
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
    if s == "":
        return 0
    else:
        num = 0
        for c in s:
            num = num + (ord(c) - ord('0'))
        return num

string = input("Enter a string: ")
result = digitSum(string)
