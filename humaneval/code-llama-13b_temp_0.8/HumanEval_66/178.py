
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
    # convert a string to a list of its characters
    # list = [char for char in s]
    # for char in list:
    #     if char.isupper():
    #         sum += ord(char)
    # return sum

    # Alternative solution:
    # .isupper() returns True if the character is upper case
    return sum(ord(c) for c in s if c.isupper())
