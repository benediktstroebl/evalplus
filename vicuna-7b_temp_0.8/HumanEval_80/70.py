
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
    # Check if the string is empty
    if len(s) == 0:
        return False
    
    # Check if the string has length 1
    if len(s) == 1:
        return True
    
    # Check if the string is happy
    for i in range(1, len(s)):
        for j in range(i+1, len(s)):
            # Check if the first letter is different from the second
            if s[i:j] == s[i-1:j-1]:
                return False
        # If we have passed through all the elements and not found any consecutive same letter
        # then the string is happy
        return True
    
    # If we have reached here, then all the letters are same
    return False
