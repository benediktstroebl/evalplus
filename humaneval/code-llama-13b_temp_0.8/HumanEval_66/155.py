
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
    # convert string to a list of characters
    charList = list(s)
    # initialize the return variable
    total = 0
    # check each character in the string
    for c in charList:
        # check if the character is upper
        if c.isupper():
            # add the character to the return value
            total += ord(c)
    return total

