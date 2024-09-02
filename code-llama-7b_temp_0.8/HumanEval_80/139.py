
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
    d = {}
    for i in range(len(s)-2):
        if s[i] != s[i+1] and s[i+1] != s[i+2] and s[i] != s[i+2]:
            d[s[i]] = d.get(s[i], 0) + 1
            d[s[i+1]] = d.get(s[i+1], 0) + 1
            d[s[i+2]] = d.get(s[i+2], 0) + 1
    for key in d.values():
        if key < 3:
            return False
    return True
