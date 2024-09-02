
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
    # Your code here
    length = len(s)
    for i in range(1, length-1):
        if s[i] == s[i+1] and s[i] == s[i+2]:
            return False
    if length >= 3:
        for i in range(3, length):
            if s[i-3] == s[i-2] != s[i-1] or s[i-3] == s[i-1] != s[i]:
                return False
        return True
    return False