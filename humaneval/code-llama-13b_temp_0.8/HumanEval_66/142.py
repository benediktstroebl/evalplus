
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
    # Given
    input_str = s
    output_sum = 0

    # Processing
    if len(input_str) > 0:
        output_sum = sum([ord(char) for char in input_str if char.isupper()])
    else:
        output_sum = 0

    # Output
    return output_sum

