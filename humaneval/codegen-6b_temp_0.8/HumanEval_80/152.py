
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
    if len(s) < 3: return False

    # first setup a unique set of letters
    s = set(s)

    while len(s) > 1:
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
               s.remove(s[i])
               s.remove(s[i])
               break
        if len(s) == 1: return True
    return False
