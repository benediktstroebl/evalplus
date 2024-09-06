
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
    # this solution will not work for the "every 3 consecutive letters are distinct" part
    # if len(s) < 3:
    #     return False
    #
    # s_set = set(s)
    #
    # if len(s_set) != len(s):
    #     return False
    #
    # return True

    if len(s) < 3:
        return False

    s_set = set(s)

    if len(s_set) != len(s):
        return False

    s_len = len(s)
    for i in range(0, s_len - 2):
        if s[i] == s[i + 1] or s[i] == s[i + 2] or s[i + 1] == s[i + 2]:
            return False
    return True

