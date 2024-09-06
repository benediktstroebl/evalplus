
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
    if len(s) < 3 or not all(map(str.isupper, s)):
        return False
    elif len(s) == 3:
        return True
    else:
        for i in range(3, len(s)):
            for j in range(i + 1, len(s)):
                if s[i:j] == s[j:i + 1]:
                    return False
        return True