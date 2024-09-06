
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
    m, n = len(s), len(s) // 2
    for i in range(m):
        for j in range(n):
            if s[i*n + j] == s[i*n + j + 1]:
                return False
        for k in range(n):
            if s[i*n + k] == s[i*n + k + 1]:
                return False
    return True
