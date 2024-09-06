
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

    if len(s) >= 3:
        counter = 1
        while counter <= 3:
            if counter == 3:
                return True
            if s[counter] == s[counter-1] and s[counter] == s[counter-2] and s[counter] == s[counter-3]:
                return False
            else:
                counter += 1
    else:
        return False
