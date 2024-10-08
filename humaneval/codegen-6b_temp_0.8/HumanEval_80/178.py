
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
    if n == 1:
        return True
    if n == 2:
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                return False
        return True
    if n % 3 == 0:
        if n == 3:
             return True
        else:
            return is_happy(s[1:-1])
    else:
        return False
