
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

    s = list(s)
    count = 1
    while count < 3:
        for i in range(len(s)):
            if i + count >= len(s):
                break
            if s[i]!= s[i + count]:
                count += 1
                break
        else:
            return True
    if count == 3:
        return False

