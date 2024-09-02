
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
    s_len = len(s)

    # case 1: s is less than 3 letters long
    if s_len < 3:
        return False

    # case 2: s is more than 3 letters long, but all 3 consecutive letters are the same
    if all(s[i] == s[i + 1] == s[i + 2] for i in range(s_len - 2)):
        return False

    # case 3: s is more than 3 letters long and no 3 consecutive letters are the same
    return True

