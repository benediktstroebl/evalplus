
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
    h = set()
    for i in range(len(s)):
        if i >= 2:
            if s[i-2] + s[i-1] + s[i] in h:
                return False
        h.add(s[i])
    return True

