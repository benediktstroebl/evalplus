
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
    d = {}
    for i in range(len(s)):
        d[s[i]] += d.get(str(ord(s[i])), 0)
    return d.get(str(ord('A') - 1), 0)