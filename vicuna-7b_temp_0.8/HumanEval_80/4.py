
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
    max_dist = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i:j] == s[j:i+1]:
                max_dist = max(max_dist, len(s[i:j]) - 1)
    return max_dist >= 3 and max_dist % 3 == 0