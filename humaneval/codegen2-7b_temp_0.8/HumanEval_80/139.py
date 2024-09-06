
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
    def check_for_distinct(string):
        return len(set(string)) == len(string)
    if len(s) < 3:
        return False
    for i in range(0, len(s)-2, 3):
        if s[i]!= s[i+2]:
            return False
    return check_for_distinct(s[0::3]) and check_for_distinct(s[1::3]) and check_for_distinct(s[2::3])
