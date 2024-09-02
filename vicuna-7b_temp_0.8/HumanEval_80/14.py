
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
    n = len(s)
    distinct = True
    for i in range(n-1, -1, -1):
        for j in range(i+1, n):
            if s[i:j+1] == s[i+1:j] or s[i:j+1] == s[i+2:j+2]:
                distinct = False
                break
    return distinct
