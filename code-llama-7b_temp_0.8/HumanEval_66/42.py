
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
    sum = 0
    for i in s:
        sum += ord(i.upper())
    return sum

    #
    # s = s.replace('a', '')
    # s = s.replace('b', '')
    # s = s.replace('c', '')
    # s = s.replace('d', '')
    # s = s.replace('e', '')
    # s = s.replace('f', '')
    # s = s.replace('g', '')
    # s = s.replace('h', '')
    # s = s.replace('i', '')
    # s = s.replace('j', '')
    # s = s.replace('k', '')
    # s = s.replace('l', '')
    # s = s.replace('m', '')
    # s = s.replace('n', '')
    # s = s.replace('o', '')
    # s = s.replace('p', '')
    # s = s.replace('q', '')
    # s = s.replace('r', '')
    # s = s.replace('s', '')
    # s = s.replace('t', '')
    # s = s.replace('u', '')
    # s = s.replace('v', '')
    # s = s.replace('w', '')
    # s = s.replace('x', '')
    # s = s.replace('y', '')
    # s = s.replace('z', '')
    # return int(s)


    # return sum([ord(i) for i in s.replace(' ', '').upper()])
    # return sum([ord(i) for i in s.replace(' ', '').upper()])


