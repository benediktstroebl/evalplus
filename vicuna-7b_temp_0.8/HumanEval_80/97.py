
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
    
    curr = s[0]
    count = 0
    for i in range(1, len(s)):
        curr = s[i]
        if curr == curr[0]:
            count += 1
        elif count % 3 == 0:
            count = 0
            curr = s[i]
        else:
            count += 1
            
    return count % 3 == 0