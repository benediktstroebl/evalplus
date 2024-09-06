
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
    # Check if the length of the string is at least 3
    if len(s) < 3:
        return False
    
    # Initialize variables to keep track of the distinct letters
    distinct_letters = set()
    
    # Loop through the string and check if every 3 consecutive letters are distinct
    for i in range(1, len(s)):
        # Check if the current letter is distinct
        if s[i] in distinct_letters:
            continue
        
        # Add the current letter to the set of distinct letters
        distinct_letters.add(s[i])
        
        # If the last letter was distinct, the string is happy
        if i < len(s) - 2:
            return True
    
    # If no distinct letters were found, the string is not happy
    return False