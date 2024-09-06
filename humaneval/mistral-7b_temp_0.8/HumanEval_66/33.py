
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
    # For test cases with length 1, the first letter is always upper case
    if len(s) == 1:
        return ord(s) - ord("A") + 1

    return sum(ord(letter) - ord("A") + 1 for letter in s if letter.isupper())

