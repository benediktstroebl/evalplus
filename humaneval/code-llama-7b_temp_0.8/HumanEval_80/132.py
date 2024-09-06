
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
    distinct_char = len(set(s))
    window_length = 3
    if distinct_char != len(s):
        return False
    for i in range(len(s) - window_length + 1):
        w = s[i:i+window_length]
        if w[0] == w[1] or w[1] == w[2] or w[0] == w[2]:
            return False
    return True

