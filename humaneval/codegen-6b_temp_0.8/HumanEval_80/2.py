
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
    s = s.lower()
    if len(s) < 3:
        return False

    def is_happy_rec(s, n):
        if len(s) < 3:
            return False
        if len(s) == 3 and len(set(s)) == 1:
            return True

        if n > len(s) - 1:
            return False
        if s[n] == s[n + 1]:
            return is_happy_rec(s[:n] + s[n + 2:], n)
        return is_happy_rec(s, n + 1)
    return is_happy_rec(s, 0)
