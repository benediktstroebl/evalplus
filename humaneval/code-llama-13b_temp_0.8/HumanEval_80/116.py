
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
    if l == 3:
        return len(set(s)) == 3
    for i in range(l - 3):
        if s[i : i + 3] in s[i + 3 :]:
            return False
    return True

