
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
    x = list(s)
    c = []
    if len(x) >= 3:
        for i in range(len(x)-2):
            if x[i] == x[i+1] == x[i+2]:
                if len(c) > 0:
                    if x[i] in c:
                        return False
                    else:
                        c.append(x[i])
            else:
                return False
    else:
        return False
    return True
