
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
    # set sum of ascii codes to 0
    sum = 0
    # loop through string
    for i in s:
        # if upper case
        if i.isupper():
            # sum += ascii code of character
            sum += ord(i)
    # return sum
    return sum
