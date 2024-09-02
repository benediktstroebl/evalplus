
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
    # initialize variables
    n = len(s)
    distinct = True
    previous = ""
    for i in range(n):
        if i % 3 == 0 and s[i] != previous:
            distinct = False
            previous = s[i]
        elif i % 3 == 1 and s[i] != previous:
            distinct = False
            previous = s[i]
        elif i % 3 == 2 and s[i] != previous:
            distinct = False
            previous = s[i]
    return not distinct
