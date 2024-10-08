
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
    distinct = 0
    for i in range(n):
        j = i + 1
        while j < n:
            if s[i] == s[j]:
                distinct -= 1
                j += 1
            else:
                distinct += 1
                j += 1
    return distinct >= 3