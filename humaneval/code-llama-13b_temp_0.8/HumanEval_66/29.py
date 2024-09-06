
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

    # We iterate over the characters
    for c in s:
        # If the ASCII code is between 65 and 90,
        # which means it's an upper character,
        # we add it to the sum
        if ord(c) > 64 and ord(c) < 91:
            sum += ord(c)

    return sum

