
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

    # Task
    # Write a function that takes a string as input and returns the sum of the upper characters'
    # ASCII codes.
    #
    # Examples:
    #    digitSum("") => 0
    #    digitSum("abAB") => 131
    #    digitSum("abcCd") => 67
    #    digitSum("helloE") => 69
    #    digitSum("woArBld") => 131
    #    digitSum("aAaaaXa") => 153

    # Create variable sum
    # variable to store the sum
    #sum = 0
    #variable to store the sum
    sum = 0
    # Create variable letters
    # letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # Create variable letters
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # For loop to go through string s
    for i in s:
        # If the character in the string is in letters
        # character in string is in letters
        if i in letters:
            # sum is equal to the sum plus the integer value of the character
            sum += ord(i)
    # Return the sum
    return sum

    # Test cases
    # Test Case 1
    # Enter the length of s
    # 10
    # Enter the string s
    # WoArBld
    # Test Case 2
    # Enter the length of s
    # 9
    # Enter the string s
    # aAaaaXa
    # Test Case 3
    # Enter the length of s
    # 0
    # Enter the string s
    #
    # Test Case 4
    # Enter the length of s
    # 12
    # Enter the string s
    # helloE
    # Test Case 5
    # Enter the length of s
    # 8
    # Enter the string s
    # woArBld
    # Test Case 6
    # Enter the length of s
    # 11
    # Enter the string s
    # abAB
