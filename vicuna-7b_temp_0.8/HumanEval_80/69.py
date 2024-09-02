
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
    count_distinct = 0
    for i in range(len(s) - 2):
        distinct = True
        for j in range(i+1, len(s)):
            if s[i] == s[j] or s[i] == s[j+1]:
                distinct = False
        if distinct:
            count_distinct += 1
    return count_distinct >= 3
