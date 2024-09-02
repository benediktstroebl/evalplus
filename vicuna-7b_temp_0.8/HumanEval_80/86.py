
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
    if len(s) < 3:
        return False
    seen = set()
    for i in range(1, len(s)):
        if s[i:i+3] == s[i+3:i+6] or s[i:i+3] == s[i+6:i+9] or s[i:i+3] == s[i+9:i+12]:
            return False
        if s[i] == s[i+1] or s[i] == s[i+2] or s[i+1] == s[i+2]:
            seen.add(s[i])
    return True

s = input().lower()
