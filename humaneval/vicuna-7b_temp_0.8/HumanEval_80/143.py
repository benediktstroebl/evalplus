
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
    # Create a list of all characters in the string
    char_list = set(s)
    
    # Create an empty list to store whether the 3 consecutive characters are distinct
    distinct_list = []
    
    # Loop through the string and check if the length is at least 3 and if every 3 consecutive characters are distinct
    for i in range(len(s)):
        # If the current character is in the list, then remove it
        if char_list.remove(s[i]):
            # Add True to the list to indicate that the 3 consecutive characters are distinct
            distinct_list.append(True)
        else:
            # If the current character is not in the list, then add False to the list to indicate that the 3 consecutive characters are not distinct
            distinct_list.append(False)
    
    # Return True if every 3 consecutive characters are distinct, otherwise return False
    return all(distinct_list)
