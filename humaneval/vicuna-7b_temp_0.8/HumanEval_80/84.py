
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
    # For the first iteration, assume the string is not happy
    happy = False
    for i in range(len(s)-1):
        if s[i:i+3] == s[i+3:i+6] or s[i:i+3] == s[i+6:i+9] or s[i:i+3] == s[i+9:i+12]:
            # If the string is not happy, return False
            return False
        if s[i:i+3] == s[i+15:i+18] or s[i:i+3] == s[i+18:i+21] or s[i:i+3] == s[i+21:i+24]:
            # If the string is not happy, return False
            return False
        if s[i:i+3] == s[i+27:i+30] or s[i:i+3] == s[i+30:i+33] or s[i:i+3] == s[i+33:i+36]:
            # If the string is not happy, return False
            return False
        if i == 0 or i == len(s)-1 or s[i-1] == s[i+1] or s[i-1] == s[i+2] or s[i-1] == s[i+3]:
            # If the string is not happy, return False
            return False
        if i == len(s)-2 or s[i-2] == s[i+2] or s[i-2] == s[i+3] or s[i-2] == s[i+4]:
            # If the string is not happy, return False
            return False
        happy = True
    return happy
