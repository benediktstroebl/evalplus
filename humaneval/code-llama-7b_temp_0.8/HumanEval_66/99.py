
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

    # Check if the input is valid
    if type(s) != str:
        return None

    # Validate the input
    # You could have used an array of invalid characters and check
    # that each character is NOT in that array

    # You could have used a regular expression to validate
    # if re.match("[A-Z]+",s)

    sum = 0
    for i in s:
        # Check if the character is in the valid range
        if ord(i) > 64 and ord(i) < 91:
            sum += ord(i)

    return sum
