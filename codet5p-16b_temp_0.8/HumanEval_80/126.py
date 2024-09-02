
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
    else:
        new_str = []
        while len(s) > 0:
            new_str.append(s[0])
            s = s[1:]
        for i in range(len(new_str)-1):
            if new_str[i] == new_str[i+1]:
                return False
        return True
