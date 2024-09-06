
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

    #Defining sum variable
    sum = 0

    #Looping through the string
    for i in s:
        #Adding to the sum only upper characters
        if i.isupper():
            sum += ord(i)

    #Returning the sum
    return sum
