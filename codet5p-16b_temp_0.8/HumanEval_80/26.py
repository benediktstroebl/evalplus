
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

    is_happy_dict = {}
    if len(s) < 3:
        return False

    for i in range(len(s)):
        if s[i] not in is_happy_dict:
            is_happy_dict[s[i]] = 1
        else:
            is_happy_dict[s[i]] += 1

    if len(is_happy_dict) == 1 and len(is_happy_dict.values()) == 1:
        return True

    for i in range(len(s)-3):
        if is_happy_dict[s[i]] == 1 and is_happy_dict[s[i+1]] == 1 and is_happy_dict[s[i+2]] == 1 and is_happy_dict[s[i+3]] == 1:
            return True

    return False

