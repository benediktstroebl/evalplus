
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
    if l % 3 != 0:
        return False
    elif not set(s[0:3]) == set(s[3:6]) == set(s[6:9]):
        return False
    elif l >= 9:
        return is_happy(s[3:9]) and is_happy(s[6:12]) and is_happy(s[9:15]) and is_happy(s[12:18])
    else:
        return True
