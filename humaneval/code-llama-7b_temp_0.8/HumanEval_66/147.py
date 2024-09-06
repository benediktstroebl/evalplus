
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
    if len(s) == 0:
        return 0
    # define a variable to store the sum
    sum = 0
    # loop through each character in the string
    for char in s:
        # if the character is upper case, add the ASCII value to the sum
        if char.isupper():
            sum += ord(char)
    # return the sum
    return sum

