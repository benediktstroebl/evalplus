
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
    # first solution
    # d = {}
    # for i, x in enumerate(s):
    #     if i > 1:
    #         if s[i-1] == s[i-2] and s[i-1] not in d:
    #             return False
    #         d[x] = 1
    # return True

    # improvement - faster
    n = len(s)
    s1 = s[0]
    for i in range(1, n//3):
        if s[i] == s1:
            return False
        s1 = s[i]
    return True
