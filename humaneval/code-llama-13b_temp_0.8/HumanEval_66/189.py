
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
    print(f"Given string: '{s}'")
    s = s.upper()
    sum = 0
    for c in s:
        if 'A' <= c <= 'Z':
            sum += ord(c)
    print(f"Sum of upper characters' ASCII codes: {sum}")
