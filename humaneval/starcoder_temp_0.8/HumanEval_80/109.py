
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
    hashmap = {}

    for i in range(len(s)):
        if i <= 2:
            hashmap[s[i]] = 1
        else:
            hashmap[s[i]] = hashmap.get(s[i], 0) + 1

        if hashmap[s[i]] == 3:
            hashmap.pop(s[i])
            if i == len(s) - 1:
                return True

    return False
