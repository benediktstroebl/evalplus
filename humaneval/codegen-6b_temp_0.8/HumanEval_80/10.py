
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
    s = s.lower()
    if n < 3:
        return False
    if s[0] != s[1] and s[2] != s[0] and s[0] != s[2]:
        return True
    if n % 3 == 0:
        return False
    for i in range(n - 3):
        if s[i] == s[i + 1] == s[i + 2] and s[i] != s[i + 3]:
            return True
    return False











