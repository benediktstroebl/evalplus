
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
        j = i + 1
        while j < len(s):
            if s[i] == s[j]:
                if i-1 < 0:
                    return False
                if i+1 > len(s):
                    return False
                if d.get(s[i-1]) or d.get(s[i+1]):
                    return False
                d[s[i]] = None
                i += 1
                j += 1
    return True