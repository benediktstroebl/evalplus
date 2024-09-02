
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
    # 1st solution
    upper_chars = list(filter(lambda x: x.isupper(), s))
    upper_chars_sum = sum([ord(c) for c in upper_chars])
    return upper_chars_sum


    # 2nd solution
    upper_chars = list(map(lambda x: ord(x), filter(lambda x: x.isupper(), s)))
    upper_chars_sum = sum(upper_chars)
    return upper_chars_sum

    # 3rd solution
    upper_chars_sum = sum(map(lambda x: ord(x), list(filter(lambda x: x.isupper(), s))))
    return upper_chars_sum

    # 4th solution
    return sum(map(lambda x: ord(x), list(filter(lambda x: x.isupper(), s))))
