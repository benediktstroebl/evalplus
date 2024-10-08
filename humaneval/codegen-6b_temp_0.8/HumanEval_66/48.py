
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
    s = s.replace(" ", "")
    sum = 0
    for i in s:
        if ord(i) > 65 and ord(i) < 91:
            sum += ord(i)
    return sum
