
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
    # convert the string to a list
    # then add up the list
    # then return that number

    # write your code here
    answer = 0

    for c in s:
        if c.isupper():
            answer += ord(c)

    return answer
