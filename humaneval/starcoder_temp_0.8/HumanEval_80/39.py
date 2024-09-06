
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
    count = Counter(s)
    while len(count) > 1:
        for i in range(len(s) - 2):
            c = s[i:i + 3]
            if count[c] == 1:
                count.pop(c)
    return len(count) == 1

