
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
    s = s.upper()
    s = s.replace(' ', '')
    s = s.replace('A', '0')
    s = s.replace('B', '1')
    s = s.replace('C', '2')
    s = s.replace('D', '3')
    s = s.replace('E', '4')
    s = s.replace('F', '5')
    s = s.replace('G', '6')
    s = s.replace('H', '7')
    s = s.replace('I', '8')
    s = s.replace('J', '9')
    s = s.replace('K', '10')
    s = s.replace('L', '11')
    s = s.replace('M', '12')
    s = s.replace('N', '13')
    s = s.replace('O', '14')
    s = s.replace('P', '15')
    s = s.replace('Q', '16')
    s = s.replace('R', '
