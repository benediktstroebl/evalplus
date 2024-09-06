
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

    if s == s[::-1]:
        return True

    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return False

    return is_happy(s[1:])

assert is_happy("a") == False
assert is_happy("aa") == False
assert is_happy("abcd") == True
assert is_happy("aabb") == False
assert is_happy("adb") == True
assert is_happy("xyy") == False
assert is_happy("abcdefghijklmnopqrstuvwxyz") == False
assert is_happy("bbb") == False
