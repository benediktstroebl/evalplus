
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
    # Check if the length of s is at least 3
    if len(s) < 3:
        return False
    
    # Check if every 3 consecutive characters are distinct
    distinct = True
    for i in range(1, len(s)):
        if s[i:i+3] == s[i-3:i+3]:
            distinct = False
            break
    return distinct
