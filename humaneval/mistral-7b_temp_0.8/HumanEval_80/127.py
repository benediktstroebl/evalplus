
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
    n = len(s)
    if n < 3:
        return False
    # The main idea here is that we only need to check the first three characters
    # and the rest of the string will be considered happy if it's the same as the first three
    # characters.
    # We also check if the string is all the same characters.
    first_chars = s[:3]
    rest = s[3:]
    if first_chars == s and s == s[3:]:
        return True
    # If the string is longer than 3 characters, we can break the string into
    # consecutive chunks of three characters and check if each chunk is distinct
    # We don't need to check the entire string since if we have a chunk of three
    # that is not distinct, we can break out of the loop since the string cannot be happy
    for i in range(0, len(s) - 2, 3):
        if s[i:i + 3] == s[i + 3:i + 6] or s[i:i + 3] == s[i + 
