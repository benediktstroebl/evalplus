
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
        arr = [int(chr(x)) for x in s]
        d = {}
        for x in arr:
            if x not in d:
                d[x] = 1
            else:
                d[x] += 1
        print(d)
        for x in d:
            if d[x] % 3 == 0 and d[x]!= 0:
                return False
            else:
                return True
    else:
        return False

