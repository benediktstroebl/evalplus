
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
    def good_3(s):
        return s[0] != s[1] and s[1] != s[2] and s[0] != s[2]
    if len(s) < 3:
        return False
    if not good_3(s[:3]):
        return False
    for i in range(1, len(s) - 2):
        if not good_3(s[i:i + 3]):
            return False
    return True
