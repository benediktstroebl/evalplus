
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

    if len(s) < 3:
        return False
    
    def next_letter(s):
        if len(s) <= 1:
            return ""
        s = list(s)
        if s[0] == s[1]:
            s.pop(0)
        else:
            s[0] = s[1]
            s.pop(1)
        return ''.join(s)

    while True:
        s = next_letter(s)
        if s == "":
            return True
        elif len(s) < 3:
            return False
        else:
            if next_letter(s) == "":
                return True
            s = next_letter(s)
            if next_letter(s) == "":
                return True
