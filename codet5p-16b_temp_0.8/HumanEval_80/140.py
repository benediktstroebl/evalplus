
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

    s = list(s)
    if len(s) >= 3 and s[2] == s[3] and s[3] == s[4]: # s[2] is the first consecutive characters
        return False
    else:
        return True
