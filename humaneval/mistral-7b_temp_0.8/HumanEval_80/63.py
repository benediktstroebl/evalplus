
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
    string = s
    if len(string) <= 2:
        return False
    for i in range(0, len(string) - 2):
        if string[i] == string[i + 1] and string[i + 1] == string[i + 2]:
            return False
    return True
