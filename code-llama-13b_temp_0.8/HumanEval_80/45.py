
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
    # position = 2
    # if len(s) < 3:
    #     return False
    # else:
    #     while position + 3 <= len(s):
    #         if s[position] == s[position + 1] and s[position] == s[position + 2]:
    #             return False
    #         else:
    #             position = position + 3
    #     return True

    if len(s) < 3:
        return False
    else:
        return is_happy(s[1:] + s[0])

