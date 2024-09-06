
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
        c = s[i]
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    for i in range(3, n):
        if d[s[i-3]] == d[s[i-2]] and d[s[i-2]] == d[s[i-1]]:
            d[s[i-3]] -= 1
            d[s[i-2]] -= 1
            d[s[i-1]] -= 1
            if d[s[i-3]] == 0 and d[s[i-2]] == 0 and d[s[i-1]] == 0:
                return True
    return False
