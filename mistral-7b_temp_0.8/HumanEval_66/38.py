
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

    # Solution 1
    '''
    output = 0
    for i in s.upper():
        if i.isalpha():
            output += ord(i) - 64
    return output
    '''

    # Solution 2
    return sum(c.isupper() and ord(c) - 64 or 0 for c in s)
