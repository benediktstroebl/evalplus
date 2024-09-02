
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
    # An array to hold the digits
    sum = 0

    # Loop through each character of the string
    for letter in s:
        # If the character is upper case, add it's ASCII value to sum
        if letter.isupper():
            sum += ord(letter)
    return sum

