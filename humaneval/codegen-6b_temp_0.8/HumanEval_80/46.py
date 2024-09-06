
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
    if len(s) == 3:
        return False
    else:
        i = 0
        count = 0
        while i <= len(s)-3:
            if s[i] == s[i+1] and s[i+1] == s[i+2]:
                count += 1
            i += 1
        if count > 0:
            return False
        else:
            return True

