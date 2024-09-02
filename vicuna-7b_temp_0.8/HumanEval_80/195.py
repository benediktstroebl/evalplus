
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
    # check if the string is at least 3 characters long
    if len(s) < 3:
        return False
    
    # check if every 3 consecutive letters are distinct
    distinct = True
    for i in range(1, len(s)):
        if s[i:i+3] == s[i+1:i+4] or s[i:i+3] == s[i+2:i+5] or s[i:i+3] == s[i+3:i+4] or \
           s[i:i+3] == s[i+4:i+5] or s[i:i+3] == s[i+3:i+6] or s[i:i+3] == s[i+4:i+5]:
            distinct = False
    
    return distinct