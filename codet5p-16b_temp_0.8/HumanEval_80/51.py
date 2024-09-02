
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
    count = {}
    for c in s:
        if c not in count:
            count[c] = 0
        count[c] += 1
        if count[c] == 3:
            count[c] = 0
            if len(count) > 3:
                return False
    return len(count) == 3
