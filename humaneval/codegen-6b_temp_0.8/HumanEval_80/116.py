
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
    len_s = len(s)
    if len_s < 3:
        return False

    s_list = list(s)
    len_s_2 = len(s_list)
    for i in range(1, len_s_2):
        if s_list[i - 1] == s_list[i]:
            return False
    return True

