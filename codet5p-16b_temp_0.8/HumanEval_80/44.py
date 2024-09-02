
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

    previous = ''
    while len(s) >= 3 and s!= previous:
        previous = s
        s = ''.join(sorted(s))
        s = sum([int(s[i]) for i in range(len(s)) if i % 3 == 0])
    return s == 1

