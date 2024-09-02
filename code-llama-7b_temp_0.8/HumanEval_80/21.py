
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
    #base case
    if len(s)<3:
        return False
    #recursive case
    else:
        start = s[0]
        end = s[2]
        middle = s[1]
        if start == end or start == middle or end == middle:
            return False
        return is_happy(s[1:])

