
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
    # My solution - Brute force - TLE
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)

    # For every index
    for i in range(len(s)):
        if i < len(s)-2 and s[i] == s[i+1] == s[i+2]:
            return False
        else:
            s = s.replace(s[i], "", 1)
    return True

