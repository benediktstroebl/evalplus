
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
    d = {}
    for i in range(n):
        if i % 3 == 0:
            j = i - 1
            while j >= 0 and s[j] == s[i]:
                j -= 1
            if j < 0:
                return False
        for k in range(i+1, n):
            if s[i] == s[k]:
                return False
    return True
