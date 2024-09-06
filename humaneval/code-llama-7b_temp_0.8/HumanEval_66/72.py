
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
    # s = s.upper()
    # # s = s.replace("A", "10")
    # # s = s.replace("B", "11")
    # # s = s.replace("C", "12")
    # # s = s.replace("D", "13")
    # # s = s.replace("E", "14")
    # # s = s.replace("F", "15")
    # # s = s.replace("G", "16")
    # # s = s.replace("H", "17")
    # # s = s.replace("I", "18")
    # # s = s.replace("J", "19")
    # # s = s.replace("K", "20")
    # # s = s.replace("L", "21")
    # # s = s.replace("M", "22")
    # # s = s.replace("N", "23")
    # # s = s.replace("O", "24")
    # # s = s.replace("P", "25")
    # # s = s.replace("Q", "26")
    # # s = s.replace("R", "27")
    # # s = s.replace("S", "28")
    # # s = s.replace("T", "29")
    # # s = s.replace("U", "30")
    # # s = s.replace("V", "31")
    # # s = s.replace("W", "32")
    # # s = s.replace("X", "33")
    # # s = s.replace("Y", "34")
    # # s = s.replace("Z", "35")
    # # print(s)
    # print(sum([int(c) for c in s.replace("A", "10")
    #            .replace("B", "11")
    #            .replace("C", "12")
    #            .replace("D", "13")
    #            .replace("E", "14")
    #           
