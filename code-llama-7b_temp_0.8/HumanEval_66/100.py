
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
    # Take a string as input
    # If string is blank, return 0
    # If string is not blank, split the string into a list
    # Create an empty string variable to hold the characters to sum
    # For each character in the string, if the character is uppercase, add the ascii value of the character to the string
    # Split the string into a list using the empty string as a delimiter
    # Convert the list into an int
    # Return the sum of the int

    if s == "":
        return 0
    elif len(s) == 1:
        if s.isupper():
            return ord(s)
        else:
            return 0
    else:
        sum = ""
        for char in s:
            if char.isupper():
                sum += chr(ord(char))
        return sum

    # create an empty string
    # for each character in the string, if the character is uppercase, add it to the empty string
    # return the empty string

    # create an empty string
    # for each character in the string, if the character is uppercase, add the ascii value of the character to the empty string
    # return the empty string

    # create an empty string
    # for each character in the string, if the character is uppercase, add the ascii value of the character to the empty string
    # return the empty string
