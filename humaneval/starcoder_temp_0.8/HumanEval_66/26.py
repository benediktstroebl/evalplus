
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

    # Initializing result
    res = 0

    # Iterating through the string
    for i in s:
        # Checking if current character is upper case
        if i.isupper():
            # If current character is upper case
            # Adding ASCII value of current character to result
            res += ord(i)

    # Returning result
    return res

