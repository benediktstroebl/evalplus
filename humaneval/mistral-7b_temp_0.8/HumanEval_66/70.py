
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
    # Code
    # 1.Declare sum variable and initialize it with 0.
    # 2.Iterate over the string.
    # 3.If the character is a uppercase character, add its ASCII value to the sum.
    # 4.Return the sum at the end.

    sum = 0
    for letter in s:
        if letter.isupper():
            sum += ord(letter)

    return sum

