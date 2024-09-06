
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
    if s == "":
        return False
    s = s.lower()
    s_dict = {}
    for c in s:
        if c in s_dict:
            s_dict[c] += 1
        else:
            s_dict[c] = 1
    for c in s:
        if s_dict[c] < 3:
            return False
        else:
            s_dict[c] = 0
    return True

