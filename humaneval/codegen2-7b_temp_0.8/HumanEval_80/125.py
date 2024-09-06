
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
    if s == "" or len(s) < 3:
        return False

    l = [False] * len(s)

    for i in range(1, len(s)-1):
        if not l[i]:
            if s[i-1] == s[i] or s[i] == s[i+1]:
                continue
            else:
                l[i] = True

    return l[0] and l[-1
