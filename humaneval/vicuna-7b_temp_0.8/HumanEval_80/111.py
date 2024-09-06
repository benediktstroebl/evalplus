
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
    for i in range(n-1):
        j = i + 1
        if j < n:
            if s[i].lower() == s[j].lower():
                break
        else:
            k = i + 1
            while k < n and s[i].lower() == s[k].lower():
                k += 1
            if k - i > 2:
                d[i] = [s[i], s[k]]
                k += 1
    for i in d:
        c = d[i][0]
        while c in d:
            c = d[c][0]
        if c in d:
            return False
    return True