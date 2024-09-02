
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
    # We will iterate through the input string and check if each letter is distinct
    x1 = 0
    x2 = 0
    x3 = 0
    for c in s:
        x1 = x1 + ord(c) - 96
    for c in s:
        x2 = x2 + (ord(c) - 96) * x1
        x1 = x1 - (ord(c) - 96)
    x3 = x1 * x2
    # Remove leading zeros and compare to 3
    if len(str(x3)) > 3 or len(str(x3)) <= 0:
        return False
    else:
        return True

