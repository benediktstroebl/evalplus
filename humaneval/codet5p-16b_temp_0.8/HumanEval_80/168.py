
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
    s_set = set(s_list)
    if len(s_set) < 3:
        return False

    while True:
        s_dict = {}
        for i in s_list:
            s_dict[i] = s_dict.get(i, 0) + 1
        s_set = set()
        for key, value in s_dict.items():
            if value >= 3:
                s_set.add(key)
        if len(s_set) == 0:
            return True
        else:
            s_list = []
            for i in s:
                s_list.append(i)
