
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
        s_list = [ch for ch in s]
        for i in range(len(s_list)-2):
            if s_list[i] == s_list[i+1] or s_list[i] == s_list[i+2]:
                return False
        return True
    else:
        return False
