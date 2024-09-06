
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

    # Create an empty string
    upper_sum = ""
    # loop through the input string
    for char in s:
        # if the character is uppercase add it to the string
        if char.isupper():
            upper_sum += char

    # convert the string to a list
    upper_sum = list(upper_sum)
    # loop through the list
    for index, char in enumerate(upper_sum):
        # convert the character to an integer
        char = int(char)
        # add the integer to the total
        upper_sum[index] = char

    total = sum(upper_sum)

    return total

