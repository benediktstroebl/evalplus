
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

    def has_consecutive_repeats(l):
        return len([x for x in l if x == l[0]]) >= 3

    if len(s) < 3:
        return False
    else:
        s = s.lower()
        s = list(s)
        while len(s) > 1:
            s = [x for x in s if x!= s[0]]
            if has_consecutive_repeats(s):
                return True
            else:
                s = [s[i] + s[i+1] for i in range(0, len(s)-1)]
        return False
