
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
    #a = string.ascii_uppercase
    #b = [ord(i) for i in s.upper()]
    #c = [i for i in b if i in a]
    #d = sum(c)
    #return d

    return sum([ord(i) for i in s.upper() if ord(i) < 91])
