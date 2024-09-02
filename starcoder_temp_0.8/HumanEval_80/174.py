
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
    h = {}
    for i, c in enumerate(s):
        if c in h:
            # already seen a repetition
            return False

        # try to find if the next 3 consecutive chars are the same
        if i < len(s) - 2:
            if s[i + 1] == s[i + 2] and s[i] == s[i + 1]:
                h[c] = 1

        # try to find if the next 2 consecutive chars are the same
        if i < len(s) - 1:
            if s[i] == s[i + 1]:
                h[c] = 1

    return len(h.keys()) >= 3

