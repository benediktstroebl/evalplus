
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
    def digit_sum(s):
        """Returns the sum of the upper characters ASCII codes in a string."""
        return sum(ord(char) for char in s if char.isupper())

    return digit_sum(s)
