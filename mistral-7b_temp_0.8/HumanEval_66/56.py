
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

    """Solution"""

    # 1st:
    # Initialize a variable to store the sum
    # Iterate over the input string and add the upper case characters'
    # ASCII codes to the sum
    # Return the sum

    # 2nd:
    # Convert the input string to uppercase
    # Iterate over the input string and add the ASCII codes of the characters to the sum
    # Return the sum

    # 3rd:
    # Convert the input string to uppercase
    # Use list comprehension to get the ASCII codes of the upper case characters in the input string
    # Sum the ASCII codes of the upper case characters in the input string
    # Return the sum

    # 4th:
    # Use the string.ascii_uppercase method to get the ASCII codes of the upper case characters
    # Use the string.ascii_lowercase method to get the ASCII codes of the lower case characters
    # Convert the input string to uppercase
    # Use list comprehension to get the ASCII codes of the upper case characters in the
