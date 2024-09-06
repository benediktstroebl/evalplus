
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

    # Convert the string to upper case
    s = s.upper()

    # Initialize the sum
    sum = 0

    # Loop through the string and add the ASCII code of each upper character to the sum
    for char in s:
        if char.isupper():
            sum += ord(char)

    # Return the sum
    return sum
