
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
    for i in range(0, len(s), 3):
        if set(s[i:i+3]) == {s[i+3], s[i+6], s[i+9]} or \
           set(s[i+3:i+9]) == {s[i], s[i+6], s[i+9]} or \
           set(s[i+6:i+9]) == {s[i], s[i+3], s[i+9]} or \
           set(s[i+9:i+15]) == {s[i+15], s[i+12], s[i+9]} or \
           set(s[i+15:i+18]) == {s[i+18], s[i+15], s[i]}:
            return False
    return True

s = input()
