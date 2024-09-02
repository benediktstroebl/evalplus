
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
    if s == "":
        return False

    slow_pointer = 0
    fast_pointer = 0
    count = 0

    while slow_pointer < len(s):
        if count == 3:
            return True
        if fast_pointer >= len(s):
            return False
        if s[slow_pointer] == s[fast_pointer]:
            slow_pointer += 1
            fast_pointer += 1
            count += 1
            continue
        else:
            return False

