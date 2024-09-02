
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
    distinct = [0, 0, 0]
    for i in range(n):
        for j in range(i+1, n):
            distinct[0] += 1
            distinct[1] += 1
            distinct[2] += 1
            if distinct[0] == distinct[1] == distinct[2]:
                distinct[0] = 0
                distinct[1] = 0
                distinct[2] = 0
    return distinct[0] >= 3 and (distinct[0] == distinct[1] or distinct[0] == distinct[2] or distinct[1] == distinct[2])
