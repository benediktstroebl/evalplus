
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

    char_map = {}
    while len(char_map) < len(s):
        for c in s:
            if c not in char_map:
                char_map[c] = 1
            else:
                char_map[c] += 1

    if len(char_map) == len(s):
        return True

    for k, v in char_map.items():
        if v % 3!= 0:
            return False

    return True


