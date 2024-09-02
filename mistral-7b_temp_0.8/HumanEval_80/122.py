
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
    # Calculate the length of the string
    length = len(s)

    # Check if the length is at least 3
    if length < 3:
        return False

    # Check if every 3 consecutive letters are distinct
    for i in range(length - 2):
        if s[i] == s[i + 1] and s[i + 1] == s[i + 2]:
            return False

    # If all conditions are met, the string is happy
    return True
