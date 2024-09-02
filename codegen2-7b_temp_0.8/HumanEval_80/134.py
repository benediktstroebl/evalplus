
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
    if s == "" or s == " ":
        return True
    if len(s) < 3:
        return False
    counter = 0
    while counter < len(s):
        if s[counter] == s[counter + 1] and s[counter] == s[counter + 2]:
            counter += 3
            continue
        else:
            return False
    return True
