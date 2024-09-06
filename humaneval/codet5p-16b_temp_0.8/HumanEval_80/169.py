
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

    
    s = list(s)
    i = 0
    while i < len(s):
        if i < len(s) - 2:
            if s[i] == s[i+1] and s[i] == s[i+2]:
                s[i] = 'x'
                s[i+1] = 'x'
                s[i+2] = 'x'
                i += 3
            else:
                i += 1
        else:
            i += 1

    if len(set(s)) < 3:
        return True
    else:
        return False
