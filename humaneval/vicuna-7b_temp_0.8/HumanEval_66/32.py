
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
    # Define the function
    def digitSum(s):
        # Create a new string with uppercase characters
        upper_s = s.upper()
        # Initialize a variable to hold the sum
        total = 0
        # Iterate through the string
        for char in upper_s:
            # Add the current character to the sum
            total += ord(char)
        return total
    # Call the function with the given string
    return digitSum(s)
