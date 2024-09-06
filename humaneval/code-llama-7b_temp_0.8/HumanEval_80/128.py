
def is_happy(s):
    """You are given a string s.
    Your task is to check if the string is happy or not.
    A string is happy if its length is at least 3 and every 3 consecutive letters are distinct
    For example:
    is_happy(a) => False
    is_happy(aa) => False
    is_happy(abcd) => True
    is_happy(aabb) => False
    is_happy(adb) => True
    is_happy(xyy) => False
    """

    if len(s) < 3:
        return False

    # loop over s
    for index, letter in enumerate(s):
        # if letter is not equal to the letter before and after, return True
        if s[index] != s[index-1] and s[index] != s[index+1]:
            return True
        # if there are not 3 consecutive letters, return false
        if index == len(s)-1:
            return False

