
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
    # Check if length of the string is at least 3
    if len(s) < 3:
        return False
    
    # Initialize a counter variable to keep track of the number of distinct letters
    num_distinct = 0
    
    # Iterate over the string
    for i in range(len(s)):
        # Get the current substring
        sub = s[i:i+3]
        
        # Check if all 3 letters are distinct
        if len(set(sub)) == 3:
            num_distinct += 1
        
    # Return True if the number of distinct letters is at least 3
    return num_distinct >= 3
