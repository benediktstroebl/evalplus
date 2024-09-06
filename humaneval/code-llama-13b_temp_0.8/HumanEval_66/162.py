
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

    sum = 0
    for c in s:
        #print("c: %s, ord(c): %d" % (c, ord(c)))
        if 'A' <= c and c <= 'Z':
            sum += ord(c)
            #print("c: %s, ord(c): %d, sum: %d" % (c, ord(c), sum))
    return sum

