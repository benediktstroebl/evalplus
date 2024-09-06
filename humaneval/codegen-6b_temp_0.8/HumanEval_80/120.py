
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
    last = s[0:3]
    new_s = s[3:]
    while new_s:
        if new_s[0] in last:
            new_s = new_s[1:]
            if not new_s:
                return False
        else:
            last = new_s[:3]
            new_s = new_s[3:]
    return True

