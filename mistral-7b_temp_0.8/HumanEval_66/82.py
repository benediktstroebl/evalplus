
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
    num = 0
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for letter in s:
        if letter.upper() in uppercase:
            num += ord(letter.upper())
    return num
