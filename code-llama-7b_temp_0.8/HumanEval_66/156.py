
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
    # ==== SOLUTION 1 ====
    # sum = 0
    # for character in s:
    #     if character.isupper():
    #         sum += ord(character)
    # return sum

    # ==== SOLUTION 2 ====
    return sum([ord(character) for character in s if character.isupper()])

    # ==== SOLUTION 3 ====
    return sum([ord(character) for character in s if character.isupper()])

