
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
    # Check length
    if len(s) < 3:
        return False
    
    # Create a dictionary to store the distinct letters
    distinct_letters = set()
    
    # Loop over the string
    for i in range(len(s)):
        # Get the current substring
        substring = s[i:i+3]
        
        # Check if the substring is distinct
        if len(substring) == 3:
            distinct_letters.update(substring)
        else:
            # The substring is not distinct, so reset the dictionary
            distinct_letters = set()
            
        # If the current substring is distinct, then the string is happy
        if len(distinct_letters) == 3:
            return True
    
    # If no substring was distinct, then the string is not happy
    return False
