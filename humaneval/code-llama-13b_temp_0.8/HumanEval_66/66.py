
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

    if s == "":
        return 0
    elif s == None:
        return 0
    else:
        return sum([ord(c) for c in s if c.isupper()])

    """
    Filtering the string before summing the values with comprehension list
    """
    # return sum([ord(c) for c in filter(lambda x: x.isupper(), s)])

    """
    Filtering the string before summing the values with for loop
    """
    # temp = []
    # for c in s:
    #     if c.isupper():
    #         temp.append(ord(c))
    # return sum(temp)

    """
    Filtering the string before summing the values with for loop with if else
    """
    # sum = 0
    # for c in s:
    #     if c.isupper():
    #         sum += ord(c)
    # return sum


    # return sum([ord(c) for c in s if c.isupper()])

    # return sum(map(ord, [c for c in s if c.isupper()]))



