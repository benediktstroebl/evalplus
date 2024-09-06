
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

    if len(s) >= 3:
        l = list(s)
        if l[0]!= l[1] and l[0]!= l[2]:
            return is_happy(s[1:]+l[0])
        else:
            return False
    else:
        return True
