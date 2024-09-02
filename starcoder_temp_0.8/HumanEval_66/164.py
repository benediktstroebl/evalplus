
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

    # initialize sum to 0
    sum = 0

    # loop through characters in string
    for char in s:
        # if character is an uppercase character, add its ascii value to sum
        if char.isupper():
            sum += ord(char)

    # return the sum of the upper characters
    return sum
