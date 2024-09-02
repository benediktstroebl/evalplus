
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

    set_letters = set()
    for index in range(len(s)):
        if index == 0:
            set_letters.add(s[index])
            continue
        set_letters.add(s[index])
        if len(set_letters) < 3:
            continue
        set_letters.remove(s[index - 2])
    if len(set_letters) < 3:
        return False
    return True

