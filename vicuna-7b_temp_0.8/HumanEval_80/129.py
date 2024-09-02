
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
    m = 0
    distinct = set()
    for i in range(n):
        if i % 3 == 0:
            m += 1
            distinct.clear()
        for j in range(i+1, n):
            if j % 3 == 0:
                m += 1
            if s[i:j] in distinct:
                m += 1
                distinct.remove(s[i:j])
        if m >= 3:
            return True
    return False