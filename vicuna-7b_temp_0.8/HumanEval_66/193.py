
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
    # Check if the input string is empty
    if len(s) == 0:
        return 0

    # Append each character to a list
    char_list = list(s)

    # Initialize sum to 0
    sum = 0

    # Iterate through the list and add the upper ASCII characters to the sum
    for char in char_list:
        sum += ord(char)

    return sum
