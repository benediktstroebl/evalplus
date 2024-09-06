
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

    # YOUR CODE HERE
    # convert string to upper case
    s = s.upper()

    # calculate sum
    sum = 0
    for c in s:
        if c.isalpha():
            sum += ord(c) - ord('A') + 1

    return sum
