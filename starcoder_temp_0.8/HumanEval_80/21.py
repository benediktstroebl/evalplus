
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

    current = s
    while len(current) > 1:
        if is_even(len(current)):
            current = current[::2]
        else:
            current = current[1::2]
        if len(set(current))!= len(current):
            return False
    return True

