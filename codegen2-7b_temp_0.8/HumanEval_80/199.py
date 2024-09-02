
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
    def helper(s, pos, count, n, res):
        if pos == n:
            return count == 3
        if count == 3:
            return True
        count += 1
        return helper(s, pos + 1, count, n, res) or helper(s, pos + 1, 0, n, res)

    return helper(s, 0, 0, len(s), {})

