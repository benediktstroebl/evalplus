
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
    if len(s) < 3:
        return False
    # let's find the longest suffix that is happy
    longest_suffix = s
    while longest_suffix:
        longest_suffix = longest_suffix[1:]
        # print(longest_suffix)
        # if the longest suffix is happy - we can use it and exit
        if is_happy(longest_suffix):
            return True
    return False

