
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
    l = len(s)
    if l < 3:
        return False
    a, b, c = s[0], s[1], s[2]
    for i in range(3, l):
        if s[i]!= s[i - 1]:
            if not (s[i - 1] == a and s[i] == b):
                return False
    return True
