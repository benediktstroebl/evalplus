
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
    l = len(s)
    d = {}
    for i in range(1, l):
        for j in range(i+1, l):
            if s[i:j] in d:
                d[s[i:j]] += 1
            else:
                d[s[i:j]] = 1
    for k in range(1, l):
        for i in range(k+1, l):
            if d[s[i:k+1]] == 1 and d[s[i:k+1]] == d[s[k+1:i]] + 1:
                d[s[i:k+1]] -= 1
    return d