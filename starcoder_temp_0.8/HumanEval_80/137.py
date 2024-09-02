
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
    if len(s) < 3:
        return False
    x = y = z = 0
    for char in s:
        if char == "x":
            x += 1
        elif char == "y":
            y += 1
        elif char == "z":
            z += 1
    return x == y and y == z

