
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
    # O(n^3) time
    # O(1) space
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            for k in range(j+1, len(s)):
                if s[i:j] == s[j:k] or s[i:k] == s[k:j]:
                    return False
    return True