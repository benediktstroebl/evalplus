
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

    # Make all uppercase letters
    s = s.upper()
    total = 0

    # For loop through s, if the character is in range of uppercase letters, sum it
    for i in s:
        if ord(i) > 64 and ord(i) < 91:
            total += ord(i)
    return total
