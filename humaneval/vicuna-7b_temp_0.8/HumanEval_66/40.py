
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
    # convert string to lowercase and store in a list
    list_ = list(map(chr, s))
    # remove the last empty list
    list_ = list_[:-1]
    # calculate the sum of uppercase characters
    sum = 0
    for i in list_:
        sum += ord(i) - ord('a' + str(len(list_)))
    return sum
