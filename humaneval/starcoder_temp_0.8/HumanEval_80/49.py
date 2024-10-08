
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
    while True:
        s = s.replace(s, s[0])
        if len(s) == 1:
            return True
        if len(s) == 2:
            return s == 'ab'
        if len(s) == 3:
            return s == 'a'
        if len(s) == 4:
            return s == 'b'
