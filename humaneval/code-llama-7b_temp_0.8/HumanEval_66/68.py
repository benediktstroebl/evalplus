
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

    # 🚨 Don't change the code below 👇
    number = "".join(c if c.isupper() else "" for c in s)
    # 🚨 Don't change the code above 👆

    #Write your code below this row 👇

    sum = 0
    for i in range(len(number)):
        sum += ord(number[i])
    return sum

