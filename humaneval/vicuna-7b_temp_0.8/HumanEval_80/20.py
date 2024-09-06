
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
    s_length = len(s)
    distinct = 0
    for i in range(1, s_length):
        for j in range(i+1, s_length):
            if s[i] == s[j]:
                distinct -= 1
        if distinct < 3:
            return False
    return True
