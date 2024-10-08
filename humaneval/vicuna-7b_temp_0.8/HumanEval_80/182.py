
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
    s_chars = set(s)
    if len(s) < 3 or len(s) % 3 != 0:
        return False
    for i in range(0, len(s), 3):
        if s_chars[i] == s_chars[i+1] and s_chars[i] == s_chars[i+2]:
            return False
    return True