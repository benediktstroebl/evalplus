
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
    seen = set()
    for i, c in enumerate(s):
        if i % 3 == 0:
            j = i + 1
            while j < len(s) and s[j] == c:
                j += 1
            if j - i > 2:
                return False
            seen.add(c)
    return True

s = "adcaba"
