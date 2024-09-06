
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
    l = s.lower()
    n = len(l)
    if n < 3:
        return False

    if l[0] == l[1] == l[2]:
        return True
    if l[0] == l[1] or l[0] == l[2] or l[1] == l[2]:
        return True

    for i in range(3, n):
        if l[i] not in l[i - 3:i + 1]:
            return False
    return
