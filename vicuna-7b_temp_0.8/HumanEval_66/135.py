
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
    # check if input is empty
    if len(s) == 0:
        return 0

    # add up the ASCII codes of the uppercase characters in the input string
    sum = 0
    for char in s:
        if char.isupper():
            sum += ord(char) - ord('A') + 1
    return sum
