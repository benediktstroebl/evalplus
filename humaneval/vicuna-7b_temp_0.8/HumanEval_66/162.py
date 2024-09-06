
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
    # Implementation of the function
    ascii_chars = set(range(97, 123)) # set of ASCII characters 97 (a) to 122 (z)
    sum = 0
    for char in s:
        sum += ord(char) - ord('a') - ord('A')
    return sum
