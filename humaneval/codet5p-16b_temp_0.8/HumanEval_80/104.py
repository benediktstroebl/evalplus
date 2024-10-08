
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
    s_list = list(s)
    while len(s_list) > 1:
        s_list = list(map(lambda x: str(ord(x))[:-1], s_list))
        while len(s_list) > 1:
            if s_list[0] == s_list[1]:
                s_list.pop(0)
                s_list.pop(1)
                s_list = list(map(lambda x: str(ord(x))[:-1], s_list))
            else:
                break
        if len(s_list) > 1:
            return False
    return True
