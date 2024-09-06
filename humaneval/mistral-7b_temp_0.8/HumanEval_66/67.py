
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

    #We create the empty list to store the sum of the upper characters only
    digitSumList=[]

    #We loop through the string passed as a parameter to add the upper character's ASCII value to our list
    for i in s:
        if (ord(i) >= 65 and ord(i) <= 90):
            digitSumList.append(ord(i))

    #We then calculate the sum of the values in the list
    sum=0
    for i in digitSumList:
        sum=sum+i

    #Return the sum
    return sum
