
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
    if not s:
        return 0
    else:
        s = s.upper()
        result = 0
        for i in range(len(s)):
            if i == 0:
                result += int(s[i])
            elif i == len(s)-1:
                result += int(s[i])
            else:
                result += int(s[i-1]) + int(s[i])
        return result
