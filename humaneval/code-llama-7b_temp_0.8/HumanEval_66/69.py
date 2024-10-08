
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
    result = 0
    for ch in s:
        # If the character is a capital letter, it has an ASCII value between 65 and 90
        if 65 <= ord(ch) <= 90:
            result += ord(ch)
    return result

