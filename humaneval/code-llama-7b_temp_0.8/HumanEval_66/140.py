
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

    # 1) we take the input
    # 2) we go through the string
    # 3) we take the ascii value of the character, if it is not a letter, we throw it away
    # 4) we convert the sum of the letters to integer
    # 5) we return the sum
    result = 0
    for character in s:
        ascii_val = ord(character)
        if ascii_val in range(65, 91):
            result += ascii_val
    return result
