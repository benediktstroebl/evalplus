
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

    sum = 0
    for char in s:
        if char.isalpha() and char.upper()!= char:
            sum += ord(char.upper()) - 65 + 1
        else:
            sum += ord(char) - 96

    return sum
