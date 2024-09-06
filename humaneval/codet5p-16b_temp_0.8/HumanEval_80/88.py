
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
    
    new_str = s[0]
    for c in s[1:]:
        new_str += c
        if len(new_str) >= 3:
            new_str = ''.join(sorted(new_str))
            if new_str == ''.join(sorted(new_str)):
                return True
    return False

