
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
    # Return 0 if the given string is empty
    if not s:
        return 0
    # Create a sum variable to store the sum of the string's characters
    # This is the accumulator of the loop
    sum = 0
    # For every character in the string
    for char in s:
        # Add the ASCII code of the character to the sum
        sum += ord(char.upper())
    return sum

