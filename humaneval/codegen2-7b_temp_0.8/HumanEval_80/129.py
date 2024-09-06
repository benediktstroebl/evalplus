
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
    mapping = {'a': True, 'b': True, 'c': True, 'd': True}
    temp = s[:3]
    count = 0

    for char in s[3:]:
        if char in mapping:
            count += 1
        else:
            count -= 1

        if count < 0:
            return False

    if count == 0:
        return True


