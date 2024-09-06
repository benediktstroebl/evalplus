
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
    # Use a data structure to record the last 2 letters of s
    last_2_letters = collections.defaultdict(int)
    for i in range(len(s)-2):
        first = s[i]
        second = s[i+1]
        third = s[i+2]
        last_2_letters[first+second+third] = 0
    # If the first 3 last letters are same,
    # then the string is not happy
    if s[0] + s[1] + s[2] in last_2_letters:
        return False
    return True

