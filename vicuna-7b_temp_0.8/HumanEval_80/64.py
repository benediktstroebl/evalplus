
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
    
    # Create an empty list to store the distinct letters
    distinct_letters = []
    
    # Loop through the string and check if every 3 consecutive letters are distinct
    for i in range(len(s)):
        # Add the current letter to the list of distinct letters
        distinct_letters.append(s[i])
        
        # Check if the next letter is different from the current letter in the list
        if i+1 < len(s) and s[i+1] == distinct_letters[-2]:
            return False
        
        # Remove the last letter from the list of distinct letters
        distinct_letters.pop()
    
    return True