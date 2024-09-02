
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
    if not s or len(s) < 3:
        return False
    mapping = {}
    for x in s:
        mapping[x] = mapping.get(x, 0) + 1
    if mapping.values().count(2) == 1:
        return True
    return False

