
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

    def check_if_consecutive(s):
        consecutive = False
        for i in range(0, len(s) - 1):
            if s[i] == s[i+1]:
                consecutive = True
                break
        return consecutive

    def rec_check_if_happy(s):
        if len(s) < 3:
            return False
        elif check_if_consecutive(s):
            return True
        else:
            return rec_check_if_happy(s[1:-1])

    return rec_check_if_happy(s)

