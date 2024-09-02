
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
    dp = 0
    for i in range(len(s)):
        if s[i:i+3] == s[i+3:i+6] == s[i+6:i+9]:
            dp = dp + 1
    return dp >= 3