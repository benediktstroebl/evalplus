
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
    uppercase = ord('A')
    lowercase = ord('a')
    sum = 0

    for c in s:
        ascii = ord(c)
        if ascii >= uppercase and ascii <= uppercase + 26:
            sum += ascii

        elif ascii >= lowercase and ascii <= lowercase + 26:
            sum -= ascii - lowercase + uppercase

    return sum

