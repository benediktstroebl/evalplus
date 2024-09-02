
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
    for i in range(l):
        if s[i] in d:
            d[s[i]] += 1
        else:
            d[s[i]] = 1
    for i in range(l-2):
        if d[s[i]] == d[s[i+1]] and d[s[i+2]] == d[s[i+3]]:
            del d[s[i]]
            del d[s[i+1]]
            del d[s[i+2]]
            break
    return not d