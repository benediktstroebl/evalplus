
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

    assert(len(s) >= 3) # It should be at least 3 characters
    s_list = [c for c in s]
    s_set = set()
    while len(s_list) >= 3:
        s_list = [s_list[i:i+3] for i in range(0, len(s_list), 3)]
        if s_set.issuperset(set(s_list)):
            return False
        s_set = s_set.union(set(s_list))
        s_list = [c for c in s]
    return True
