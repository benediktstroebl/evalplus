
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
    a = set(list(s))
    if len(a) <= 2:
        return False
    while len(a) > 0:
        i, j = 0, 0
        while i < len(a):
            if j < len(a):
                if j == i:
                    j += 1
                else:
                    if a[i] == a[j]:
                        return False
                    else:
                        i += 1
                        j += 1
            else:
                break

        a = set(list(s))
        if len(a) <= 2:
            return False
        else:
            s = s[len(a):]
    return True

