
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
    s = s.lower()
    l = len(s)
    if l < 3:
        return False

    i = 0
    while i < l:
        char = s[i]
        if s.count(char) == 0:
            return False
        i += 2
    return True

