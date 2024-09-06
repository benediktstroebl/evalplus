
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
    buff = [s[:3]]
    for i in range(3, len(s) + 1, 3):
        if s[i - 3] == s[i - 2] and s[i - 1] == s[i]:
            buff.append(s[i - 3:i])
    return len(buff) == 0 or ((len(buff) == 1 and len(buff[0]) == 3) or
        (buff[0] == buff[1] and len(buff[1]) == 3))
