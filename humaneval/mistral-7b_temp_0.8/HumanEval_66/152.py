
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
    for char in s.upper():
        if char.isalpha():
            sum += ord(char) - 64
    return sum

    # Alternative
    return sum(map(lambda x: ord(x) - 64, s.upper()))
