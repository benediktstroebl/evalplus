
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
    if s_length < 3:
        return False
    else:
        if s_length % 3 == 0:
            for i in range(s_length-2):
                if s[i] == s[i+1] and s[i] == s[i+2]:
                    return False
            return True
        else:
            for i in range(s_length-2):
                if s[i] == s[i+1] and s[i] == s[i+2]:
                    return False
            if s[-3] == s[-2] and s[-3] == s[-1]:
                return False
            else:
                return True
