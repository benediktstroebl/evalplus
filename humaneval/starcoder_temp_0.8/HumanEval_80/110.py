
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

    def length_of_next(s):
        return sum(map(int, s[i] == s[i + 2] for i in range(len(s) - 2)))

    s = ''.join(set(s))  # drop duplicates
    while len(s) >= 3 and length_of_next(s) > 0:
        s = ''.join(set(s))
    return len(s) >= 3

