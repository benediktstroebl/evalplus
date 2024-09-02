
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
    # # O(n^2) time | O(1) space
    # for i in range(len(s)):
    #     for j in range(3):
    #         if i+j >= len(s):
    #             break
    #         if s[i+j]!= s[i]:
    #             return False
    # return True

    # O(n) time | O(1) space
    count = 0
    prev = None
    for char in s:
        if char == prev:
            count += 1
        else:
            count = 1
        prev = char
        if count > 2:
            return False
    return True
