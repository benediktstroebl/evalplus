
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
    # Check if length is at least 3
    if len(s) < 3:
        return False
    
    # Initialize a variable d with first letter of s
    d = s[0]
    
    # Check every 3 consecutive letters
    for i in range(1, len(s)):
        if i % 3 == 0:
            # Check if the 3 consecutive letters are distinct
            if d == s[i] or d == s[i-1] or d == s[i-2]:
                return False
            else:
                d = s[i]
        else:
            # Skip 3 consecutive letters
            pass
    
    # Return True if every 3 consecutive letters are distinct
    return True