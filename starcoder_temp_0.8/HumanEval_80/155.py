
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

    for i in range(len(s)):
        if s.count(s[i]) == 1:
            pass
        elif s.count(s[i]) > 1:
            print("Found one more than one")
            return False
        else:
            print("Found one more than one")
            return False

    return True

