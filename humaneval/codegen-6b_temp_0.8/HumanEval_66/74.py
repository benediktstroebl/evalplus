
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
    # Convert to upper case and remove non-ascii characters
    r = [c for c in s if ord(c) >= 65 and ord(c) <= 90]
    # Sum all the digits
    return sum(ord(c) - 64 for c in r)

