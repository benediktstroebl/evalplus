
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
    
    # Initialize a dictionary to store distinct letters
    distinct = set()
    
    # Loop through the string
    for i in range(1, len(s)):
        # Append the current character to the dictionary
        distinct.add(s[i])
    
    # Loop through the dictionary
    for i in range(1, len(distinct)):
        # Remove the current character from the dictionary
        distinct.remove(distinct[i-1])
    
    # Return True if all the characters in the dictionary are distinct
    return len(distinct) >= 3
