
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

    # keep track of last 3 chars
    # no 2 chars can be the same
    for i in range(len(s)-3):
        if s[i] == s[i+1] and s[i] == s[i+2] and s[i] == s[i+3]:
            return False

    return True


