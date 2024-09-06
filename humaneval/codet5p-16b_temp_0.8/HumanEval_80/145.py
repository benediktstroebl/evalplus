
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
    s = list(s)
    s_set = list(set(s))
    while len(s) >= 3:
        s_temp = s[0]
        s_temp += s[1]
        s_temp += s[2]
        s.pop(0)
        s.pop(0)
        s.pop(0)
        if len(s) < 3:
            if s_temp in s_set:
                return True
            else:
                return False
        s_set = list(set(s))
    return False



