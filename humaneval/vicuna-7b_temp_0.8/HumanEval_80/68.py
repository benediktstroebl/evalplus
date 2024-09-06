
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
        if s[i] in d:
            d[s[i]] += 1
        else:
            d[s[i]] = 1
    for i in range(n-2, -1, -1):
        for j in range(i+1, n):
            if s[i] == s[j]:
                d[s[i]] -= 1
                break
    return d