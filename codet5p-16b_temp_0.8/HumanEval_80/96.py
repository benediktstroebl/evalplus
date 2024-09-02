
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

    l = len(s)
    if l < 3:
        return False
    s = sorted(s)
    count = 0
    while count < l:
        if s[count]!= s[count + 1]:
            count += 1
        if count == l - 1:
            break
        if s[count] == s[count + 2] and s[count + 1] == s[count + 3]:
            return True
        count += 1
    return False
