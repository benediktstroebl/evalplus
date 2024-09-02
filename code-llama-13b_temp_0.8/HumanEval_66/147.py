
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

    upper_sum = 0
    for letter in s:
        ascii_code = ord(letter)

        if ascii_code < 65:
            ascii_code = ascii_code + 32

        if ascii_code < 91:
            upper_sum = upper_sum + ascii_code

    return upper_sum


