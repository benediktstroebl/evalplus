
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
    assert isinstance(s, str), "Input must be string."
    assert len(s) >= 3, "Input must be at least 3 characters long."

    if len(s) % 3 == 0:
        for i in range(0, len(s), 3):
            if s[i:i+3] == s[i:i+3][::-1]:
                return False
        return True
    elif len(s) % 3 == 1:
        for i in range(0, len(s) - 2, 3):
            if s[i:i+3] == s[i:i+3][::-1]:
                return False
        return True
    else:
        for i in range(0, len(s) - 1, 3):
            if s[i:i+3] == s[i:i+3][::-1]:
                return False
        return True

