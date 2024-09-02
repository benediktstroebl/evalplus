
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
    # 1st solution: using dict
    # O(n) time | O(n) space - where n is the length of s
    # check every 3 consecutive letters
    # d = {}
    # if len(s) < 3:
    #     return False
    # i = 0
    # while i <= len(s) - 3:
    #     #print(s[i:i+3],d.keys())
    #     if s[i:i+3] in d:
    #         return False
    #     else:
    #         d[s[i:i+3]] = 1
    #     i += 1
    # return True

    # 2nd solution: using set
    # O(n) time | O(n) space - where n is the length of s
    # check every 3 consecutive letters
    if len(s) < 3:
        return False
    i = 0
    s = set(s)
    while i <= len(s) - 3:
        if s[i] == s[i+1] == s[i+2]:
            return False
        i += 1
    return True
