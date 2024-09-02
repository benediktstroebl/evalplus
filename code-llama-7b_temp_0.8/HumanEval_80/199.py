
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
    string = list(s)
    for i in range(len(string)):
        if len(string) < 3:
            return False
        else:
            string.pop(0)
            if string[0] == string[1] or string[1] == string[2]:
                return False
            else:
                return True

