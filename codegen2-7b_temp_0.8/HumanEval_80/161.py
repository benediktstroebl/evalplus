
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
    l = list(s)
    count = 0
    for i in range(len(l)):
        if i+2 >= len(l) or l[i]!= l[i+2]:
            count = 0
        else:
            count += 1
        if count >= 3:
            return True
    return False


