
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
    # use a dictionary to keep track of the last 3 letters
    # if the last 3 letters are the same, it is not a happy string
    last_3 = {}
    for i in range(len(s)-2):
        if s[i:i+3] in last_3.keys():
            return False
        last_3[s[i:i+3]] = 1
    return True
