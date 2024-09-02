
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
    # 01
    # s = list(s)
    # for i in range(len(s)):
    #     if s[i] in s[:i]:
    #         return False
    # return len(s) >= 3

    # 02
    # count = 0
    # for i in s:
    #     if i in s[0:i]:
    #         count += 1
    #     if count == 3:
    #         return True
    # return len(s) >= 3

    # 03
    # count = 0
    # for i in range(len(s)):
    #     if s[i] in s[0:i]:
    #         count += 1
    #     if count == 3:
    #         return True
    # return len(s) >= 3

    # 04
    return len(s) >= 3 and len({s[i] for i in range(len(s))}) == len(s)

