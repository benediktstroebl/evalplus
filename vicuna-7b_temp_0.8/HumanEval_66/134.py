
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
    # convert the input string to a list of characters
    chars = list(s)

    # initialize the sum to 0
    sum = 0

    # iterate through the characters in the list
    for char in chars:
        # if the character is a digit, add its ASCII code to the sum
        if char.isdigit():
            sum += int(char)

    return sum
