
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
    # Write your code here
    if s is None:
        return 0

    if len(s) == 0:
        return 0

    # every time we add a new digit to the sum
    # we can use the builtin ord to get the ascii code of that character
    # we then check to make sure it is an upper case character
    # if it is, we add it to the sum. otherwise, we skip it
    return sum([ord(c) for c in s if c.isupper()])
