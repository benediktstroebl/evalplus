
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
    if n < 3:
        return False
    d = {}
    for i in range(n):
        for j in range(i+1, n):
            distinct = True
            for k in range(i+1, n):
                if s[k] == s[j]:
                    distinct = False
                    break
            if distinct:
                d[i] = d[j] = s[i]
    for i in range(n-3):
        if d[i] == d[i+1] and d[i+1] == d[i+2]:
            return False
    return True
