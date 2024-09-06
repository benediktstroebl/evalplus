
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

    def next_char(s, i):
        # note that we need to skip the first character
        if len(s) > 1 and s[i] == s[i + 1]:
            return i + 2
        else:
            return i + 1

    i = 0
    while i < len(s) and i < 2:
        i = next_char(s, i)

    while i < len(s):
        i = next_char(s, i)
        if i < len(s) and i < 2:
            return False
        i = next_char(s, i)

    return True
