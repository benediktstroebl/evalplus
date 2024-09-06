
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
    d = defaultdict(int)
    for i in range(len(s)):
        if i >= 2:
            d[s[i-2:i+1]] += 1
        else:
            d[s[i:i+3]] += 1
    return max(d.values()) <= 1

