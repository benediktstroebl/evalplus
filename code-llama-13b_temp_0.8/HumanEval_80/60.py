
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
    # To remove the first 2 elements we use s[2:]
    # The string is happy if the set of the letters is equal to the set of the letters
    return len(s) >= 3 and set(s[2:]) == set(s[:-2])

