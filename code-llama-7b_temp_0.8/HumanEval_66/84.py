
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
    # take the input and convert it to a list
    s = list(s)

    # iterate over the list 
    for i in range(len(s)):
        # convert each string to uppercase
        s[i] = s[i].upper()

    # create an empty string to store the sums
    sum = ""

    # iterate over the list again 
    for i in range(len(s)):
        # convert the integers to strings
        s[i] = str(ord(s[i]))
        # add the integers to the string
        sum = sum + s[i]

    # return the integer value of the sum
    return int(sum)
