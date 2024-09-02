
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

    # Initialize variables
    distinct = 0
    prev_chars = set()

    # Iterate over string
    for char in s:
        # Add char to set of distinct characters
        distinct += 1
        prev_chars.add(char)

    # Check if every 3 consecutive characters are distinct
    while distinct > 0:
        distinct -= 1
        if distinct % 3 == 0:
            return False

    return True
