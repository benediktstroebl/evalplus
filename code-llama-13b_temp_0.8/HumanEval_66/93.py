
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
    if not isinstance(s, str):
        raise TypeError("The input should be a string")

    # If string is empty, return 0
    if len(s) == 0:
        return 0

    # If string is not empty
    s = s.upper()
    digits = [ord(i) for i in s if i.isdigit()]
    return sum(digits)

