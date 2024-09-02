
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
    # Get the length of the input string
    n = len(s)

    # Initialize a variable to store the sum
    sum = 0

    # Iterate over the characters in the input string
    for i in range(n):
        # Add the ASCII code of the current character to the sum
        sum += ord(s[i])

    # Return the sum
    return sum
