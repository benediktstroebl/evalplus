
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
    s = set(s)
    if len(s) < 3:
        return False
    count = 1
    for i in range(n):
        if count < 3:
            count += 1
            continue
        if s[i] == s[i + 1] and s[i] == s[i + 2]:
            count += 1
        else:
            count = 1
    return count == 3 and len(set(s)) ==
