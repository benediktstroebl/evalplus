
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

    seen = {}
    for i in s:
        if i not in seen:
            seen[i] = 1
        else:
            seen[i] += 1
    for k, v in seen.items():
        if v % 3 != 0:
            return False
    return True

