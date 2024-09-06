
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
    if s[:3] == s[3:6] and s[:3]!= s[6:9]:
        return True
    if s[0:3] == s[3:6] and s[0:3]!= s[6:9]:
        return True
    if s[1:4] == s[4:7] and s[1:4]!= s[7:10]:
        return True
    if s[2:5] == s[5:8] and s[2:5]!= s[8:11]:
        return True
