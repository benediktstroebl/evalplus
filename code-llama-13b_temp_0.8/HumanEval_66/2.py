
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
    # In case it's empty, I want to return 0
    if s == "":
        return 0
    # Otherwise I count the ASCII codes of each letter
    # then I sum them all
    return sum([ord(x) for x in s if ord(x) < 97])
