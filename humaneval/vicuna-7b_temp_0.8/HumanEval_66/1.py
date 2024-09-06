
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
    ascii_map = {65: 'A', 69: 'B', 71: 'C', 73: 'D', 75: 'E', 77: 'F', 85: 'G', 87: 'H', 97: 'I', 101: 'J', 105: 'K', 108: 'L', 101: 'M', 108: 'N', 111: 'O', 110: 'P', 111: 'Q', 110: 'R', 109: 'S', 111: 'T', 105: 'U', 101: 'V', 108: 'W', 111: 'X', 111: 'Y', 111: 'Z'}
    n = len(s)
    sum = 0
    for i in range(n):
        if s[i] in ascii_map:
            sum += ascii_map[s[i]]
        else:
            sum += s[i]
    return sum