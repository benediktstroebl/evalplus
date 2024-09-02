
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
    def is_consecutive(substr):
        return len(substr) >= 3 and substr[0] != substr[1] and substr[1] != substr[2]

    if len(s) < 3:
        return False

    return is_consecutive(s) and is_consecutive(s[2:] + s[:2])
