
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
    # Check if the string is empty
    if len(s) == 0:
        return 0

    # Get the sum of the upper characters
    sum = 0
    for i in range(len(s)-1):
        sum += ord(s[i]) + ord(s[i+1])

    # Add the value of the last character
    sum += ord(s[len(s)-1])

    return sum
