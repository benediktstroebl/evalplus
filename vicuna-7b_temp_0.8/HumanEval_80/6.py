
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
    curr_len = 1
    curr_distinct = 0
    for char in s:
        curr_len += 1
        curr_distinct = 0
        for i in range(curr_len - 2):
            curr_distinct += 1
            if s[i] == s[i + 1]:
                curr_distinct -= 1
        if curr_distinct < 3:
            return False
    return True