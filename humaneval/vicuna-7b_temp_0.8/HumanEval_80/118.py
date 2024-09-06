
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
    # Check if the length is at least 3
    if len(s) < 3:
        return False
    
    # Initialize the count of distinct letters to 0
    count = 0
    
    # Loop through the string and count the distinct letters
    for i in range(1, len(s)):
        # Increment the count of distinct letters
        count += 1
        
        # Check if the current letter is distinct from the previous three letters
        if count % 3 != 0:
            return False
    
    # If the loop completes and the count of distinct letters is 3, the string is happy
    return True