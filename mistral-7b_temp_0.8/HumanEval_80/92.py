
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
    n = len(s)
    if n < 3:
        return False
    if n == 3:
        return s[0] != s[1] != s[2]
    if n == 4:
        return s[0] != s[1] and s[1] != s[2] and s[2] != s[3]
    if n == 5:
        return s[0] != s[1] and s[1] != s[2] and s[2] != s[3] and s[3] != s[4]
    if n == 6:
        return s[0] != s[1] and s[1] != s[2] and s[2] != s[3] and s[3] != s[4] and s[4] != s[5]
    if n == 7:
        return s[0] != s[1] and s[1] != s[2] and s[2] != s[3] and s[3] != s[4] and s[4] != s[5] and s
