
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
    # This is an example solution.
    # You should write your own solution
    # (the parts you need to fill in is denoted by ...)
    upper = []
    for i in s:
        if i.isupper():
            upper.append(ord(i))
    if not upper:
        return 0
    return sum(upper)

