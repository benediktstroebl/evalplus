
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
    ls = list(s)
    if len(ls) < 3:
        return False
    for i in range(len(ls) - 2):
        if ls[i] == ls[i + 1] and ls[i + 1] == ls[i + 2]:
            return False
    return True

