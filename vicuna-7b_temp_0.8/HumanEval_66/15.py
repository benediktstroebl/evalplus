
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
    # s = s.upper() #convert to uppercase
    # max = max([len(ch) for ch in s])
    # s = ''.join([chr(ord(ch) - 65) if ord(ch) > 64 else ch for ch in s])
    # s = s.translate(str.maketrans('', '', string.punctuation))
    # s = ''.join([chr(ord(ch) - 65) if ord(ch) > 64 else ch for ch in s])
    s = [ord(ch) - 64 for ch in s]
    return sum(s)

s = input()
