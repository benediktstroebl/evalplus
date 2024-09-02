
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

    s_list = list(s)
    s_set = set(s_list)
    if len(s_set) <= 2:
        return True
    if len(s_list) <= 3:
        return False
    count = 0
    for i in range(len(s_list) - 2):
        if s_list[i] == s_list[i + 1] and s_list[i] == s_list[i + 2]:
            count += 1
    if count >= 1:
        return False
    return True

