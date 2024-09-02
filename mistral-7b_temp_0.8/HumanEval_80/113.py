
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

    def is_distinct(s):
        alphabet_list = [chr(i) for i in range(97,123)]
        flag = True
        for i in range(3):
            if s[i] not in alphabet_list:
                flag = False
        for i in range(3, len(s), 3):
            if s[i] not in alphabet_list:
                flag = False
            if s[i] == s[i - 3]:
                flag = False
        if not flag:
            return False
        return True
    if len(s) < 3:
        return False
    return is_distinct(s)



