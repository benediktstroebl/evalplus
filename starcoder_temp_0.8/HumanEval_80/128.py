
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
    hash_ = {}
    for i in range(len(s)):
        if i >= 3:
            if s[i - 3] + s[i - 2] + s[i - 1] in hash_:
                if s[i - 3] + s[i - 2] + s[i - 1]!= s[i]:
                    return False
            else:
                hash_[s[i - 3] + s[i - 2] + s[i - 1]] = 1
        if i >= 2:
            if s[i - 2] + s[i - 1] in hash_:
                if s[i - 2] + s[i - 1]!= s[i]:
                    return False
            else:
                hash_[s[i - 2] + s[i - 1]] = 1
        if i >= 1:
            if s[i - 1] in hash_:
                if s[i - 1]!= s[i]:
                    return False
            else:
                hash_[s[i - 1]] = 1
    return True
