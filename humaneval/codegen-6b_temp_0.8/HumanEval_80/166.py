
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
    result = True
    if len(s) < 3:
        result = False

    char_map = {}
    for i in range(0, len(s)):
        char = s[i]
        if char not in char_map:
            char_map[char] = 1
        else:
            char_map[char] += 1

    for value in char_map.values():
        if value % 3 != 0:
            result = False
    return result

