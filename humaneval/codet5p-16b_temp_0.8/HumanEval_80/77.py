
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

    def check_pair(a, b):
        if a!= b:
            return True
        return False

    if len(s) < 3:
        return False
    else:
        prev_char = s[0]
        next_char = s[1]
        for char in s[2:]:
            if check_pair(prev_char, char) and check_pair(next_char, char):
                return False
            prev_char = char
            next_char = char
        return True

