
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

    s = list(s)
    while len(s) >= 3:
        if len(s) < 3:
            return False
        else:
            for i in range(3):
                if i == 2:
                    return True
                elif s[i] == s[i+1]:
                    s.pop(i)
                    s.pop(i)
                    break
    return True
