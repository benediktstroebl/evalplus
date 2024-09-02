
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

    # Please print out which test case is failing
    # and write the output of each test case
    # Please remove the "return" statement and modify the function
    # You can add additional variables if needed
    # The number of upper characters should be returned

    # return int(s.count("A") + s.count("B") + s.count("C") + s.count("D") + s.count("E") + s.count("F") + s.count("G") + s.count("H") + s.count("I") + s.count("J") + s.count("K") + s.count("L") + s.count("M") + s.count("N") + s.count("O") + s.count("P") + s.count("Q") + s.count("R") + s.count("S") + s.count("T") + s.count("U") + s.count("V") + s.count("W") + s.count("X") + s.count("Y") + s.count("Z"))

    # Solution 1
    # s = s.upper()
    # return int(sum([ord(i) for i in s]))

    # Solution 2
    return int(sum([ord(i) - 64 for i in s.upper() if ord(i) in range(65, 91)]))

