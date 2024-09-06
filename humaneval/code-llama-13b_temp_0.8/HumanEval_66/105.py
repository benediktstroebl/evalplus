
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

    # 1. init a variable that holds the sum
    # 2. convert the string to uppercase
    # 3. iterate over the string
    # 4. if the index is an uppercase ASCII character, add it to the sum
    # 5. return the sum

    sum = 0
    for c in s.upper():
        if c.isupper():
            sum += ord(c)
    return sum

