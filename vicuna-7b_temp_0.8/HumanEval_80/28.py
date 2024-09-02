
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
    # Use a dictionary to store the length of consecutive repeated characters
    # Initialize the dictionary with length 0
    repeated = {}
    for i in range(len(s)):
        c = s[i]
        repeated[(c, i)] = 1
        for j in range(i + 1, len(s)):
            if repeated[(c, j)] == 1:
                repeated[(c, j)] = 2
            else:
                repeated[(c, j)] = 0
    for i in range(3, len(s)):
        if repeated[(s[i-3], i-3)] == repeated[(s[i-2], i-2)] == repeated[(s[i-1], i-1)] == 0:
            return False
    return True
