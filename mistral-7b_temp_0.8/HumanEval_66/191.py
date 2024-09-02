
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
    if not s:
        return 0
    # TODO: Write your code here
    #hint: a.isupper()
    #hint: a.isdigit()
    #hint: ord(a)
    #hint: sum(list(map(lambda x: ord(x), s.upper())))
    return 0
