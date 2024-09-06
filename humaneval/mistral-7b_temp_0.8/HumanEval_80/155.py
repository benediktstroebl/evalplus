
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
    if len(s) < 3:
        return False

    # Create a dictionary to store the letters that have already been seen
    seen = {}

    # Check if all 3 consecutive letters are distinct
    for i in range(len(s) - 2):
        if s[i] in seen and s[i] == s[i + 1] and s[i + 1] == s[i + 2]:
            return False
        seen[s[i]] = True

    # Check if the last 3 letters are distinct
    for i in range(len(s) - 2, len(s)):
        if s[i] in seen and s[i] == s[i - 1] and s[i - 1] == s[i - 2]:
            return False
        seen[s[i]] = True

    return True
