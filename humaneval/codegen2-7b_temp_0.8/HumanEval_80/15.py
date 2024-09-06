
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
    if s.isnumeric():
        return False
    a = s.strip()
    length = len(a)
    if length < 3:
        return False
    x = 0
    y = 0
    while x < length - 2:
        if a[x] == a[x + 2]:
            return False
        x += 1
    return True

