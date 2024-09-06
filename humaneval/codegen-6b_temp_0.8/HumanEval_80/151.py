
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
    # If the string is at least 3 letters long
    if len(s) < 3:
        return False
    # Check for 3 consecutive letters (unless the string is already 3 or fewer characters)
    # Use collections.Counter() to get a dictionary of how many of each letter there are
    # Use the difference method to find the difference between the first and last letters
    # It should be 0 if the letters are distinct, otherwise it should be greater than 0
    return any(s[i-1] != s[i] for i in range(3, len(s)))
