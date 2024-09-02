
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
    assert len(s) >= 3
    counter = {}
    for i in range(len(s)-2):
        if s[i] == s[i+1] == s[i+2]:
            return False
        if s[i] not in counter:
            counter[s[i]] = 0
        counter[s[i]] += 1
    return len(counter) > 0

