
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
    # s = 'abc'
    n = len(s)

    # check length and concatenate last two letters to first one
    # for example 'abc' becomes 'cba'
    if n < 3 or s[0] == s[1] or s[1] == s[2]:
        return False

    s_ = s[2:] + s[0:2]

    # we check if the resulting string is equal to the original
    return s == s_

