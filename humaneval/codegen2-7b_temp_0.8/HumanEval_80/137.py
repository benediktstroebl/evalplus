
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
    count = {}
    for char in s:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    if len(count) < 3:
        return False
    for i in range(3, len(s) + 1):
        if i not in count:
            return False
    return
