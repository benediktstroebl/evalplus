
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

    s = "".join(sorted(s))
    while True:
        if s == "1":
            return True
        if s == "0":
            return False
        s = s.replace(s[0], "1", 1)
        s = s.replace(s[1], "0", 1)
        s = s[2:] + s[:2]
