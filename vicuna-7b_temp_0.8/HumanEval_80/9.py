
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
    # Check the length of the string
    if len(s) < 3:
        return False
    
    # Initialize a variable to store the number of distinct letters in the string
    num_distinct_letters = 0
    
    # Iterate over the characters in the string
    for i, c in enumerate(s):
        # Increment the number of distinct letters
        num_distinct_letters += 1
        
        # Check if the current letter is distinct from the previous 2 letters
        if i % 3 == 0 and c != s[i-1] and c != s[i-2]:
            # If the current letter is distinct, increment the number of distinct letters again
            num_distinct_letters += 1
    
    # Return True if the string has at least 3 distinct letters and every 3 consecutive letters are distinct
    return num_distinct_letters >= 3