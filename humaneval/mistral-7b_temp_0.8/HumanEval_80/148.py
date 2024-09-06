
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
    lst = []
    for i in s:
        lst.append(i)
    for i in range(0, len(lst)-2, 3):
        if lst[i] == lst[i+1] or lst[i] == lst[i+2] or lst[i+1] == lst[i+2]:
            return False
    return True

