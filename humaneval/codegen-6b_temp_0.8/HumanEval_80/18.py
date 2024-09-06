
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
    # How to count the number of distinct letters in a string
    # Using a hash map to turn a string into a list of characters
    # Count the number of distinct characters
    # Have a flag to stop the recursion
    # Have a limit to the string length
    # Run the string against the checker function
    # Return False if the count is different or the string length is less than 3
    if len(s) < 3:
        return False
    hash_map = {}
    for c in s:
        if hash_map.get(c) is None:
            hash_map[c] = True
        else:
            return False
    return True
