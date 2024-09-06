
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

    #Return 0 if there are no uppercase letters in the input
    if not s.isupper():
        return 0

    #Split the string into characters and sum the upper characters
    return sum(map(int, filter(str.isupper, list(s))))
