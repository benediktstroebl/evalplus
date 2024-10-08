
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

    hash_map = {}
    while True:
        new_s = ''.join(sorted(list(set(s))))
        if len(new_s) < 3:
            return False
        if new_s in hash_map:
            return False
        hash_map[new_s] = 1
        s = sum([ord(x) for x in s])
        s = s - (s % 3)
        s = str(s)
        if len(s) == 1:
            return True
        if s[0] == s[1] == s[2]:
            return False
        s = s[1:]

