
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

    # sort the string
    s = sorted(s)

    # if len of string is less than 3, return false
    if len(s) < 3:
        return False

    # check if all substrings of length 3 are distinct
    for i in range(len(s)-2):
        if s[i] == s[i+1] == s[i+2]:
            return False
    return True
