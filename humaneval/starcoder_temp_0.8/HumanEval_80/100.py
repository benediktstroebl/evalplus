
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

    def get_next_str(s):
        res = ''
        for i in range(len(s)):
            res += s[i]
            if i < len(s) - 2:
                res += s[i + 2]
        return res

    s_set = set()
    while s not in s_set:
        s_set.add(s)
        if len(s) < 3:
            return False
        s = get_next_str(s)
    return True

