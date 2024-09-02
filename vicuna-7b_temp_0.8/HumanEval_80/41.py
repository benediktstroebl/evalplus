
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
    # Check length of s
    if len(s) < 3:
        return False
    
    # Initialize count to 0
    count = 0
    
    # Loop over all characters in s
    for i in range(len(s)):
        # Loop over all characters in s from i+1 to end of s
        for j in range(i+1, len(s)):
            # Increment count if current and next two characters are distinct
            if j > i+1:
                if s[i:j+1] == s[j:i+1]:
                    count = 0
            count += 1
    
    # Return True if count is at least 3, otherwise False
    return count >= 3
