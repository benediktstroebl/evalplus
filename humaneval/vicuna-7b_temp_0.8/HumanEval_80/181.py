
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
    d = {}
    for i in range(len(s)):
        c = s[i:i+3]
        if len(c) >= 3 and all(c[j] != c[j+1] for j in range(1, len(c))) and c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return not any(len(d[c]) == 1 for c in d.keys())