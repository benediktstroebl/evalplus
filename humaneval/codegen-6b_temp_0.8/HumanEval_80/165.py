
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
    def is_happy_helper(s, i, j):
        distinct = len(set(list(s[i:j + 1])))
        if i == j:
            return True if len(s) >= 3 and distinct == 1 else False
        return distinct == 1 and is_happy_helper(s, i + 1, j)

    return is_happy_helper(s, 0, len(s))
