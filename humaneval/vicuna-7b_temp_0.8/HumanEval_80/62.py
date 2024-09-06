
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
    m, n = len(s), len(str(s))
    distinct = True
    for i in range(n):
        for j in range(i + 1, n):
            if s[i:j+1] == s[j+1:i+2]:
                distinct = False
                break
    return m >= 3 and distinct

s = input().strip()
