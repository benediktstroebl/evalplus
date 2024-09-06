
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
    m, n = len(s), len(reversed(s))
    if m < 3 or n < 3:
        return False
    for i in range(m-1, -1, -1):
        j = i+1
        for k in range(j-1, -1, -1):
            if s[i] == s[j] or s[i] == s[k] or s[j] == s[k]:
                return False
    return True