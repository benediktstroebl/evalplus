
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
    assert type(s) == str, "Please enter a string."
    if len(s) < 3:
        return False
    if s == s[0]:
        return False
    if s == s[::2]:
        return False
    if s == s[::3]:
        return True
    for i in range(len(s) - 2):
        if s[i] == s[i+2]:
            return False
    
