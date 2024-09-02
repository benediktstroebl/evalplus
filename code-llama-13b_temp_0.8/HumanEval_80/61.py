
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
    def is_consecutive(str):
        str = str.lower()
        for i in range(0, len(str) - 2):
            if (str[i] == str[i+1] or str[i] == str[i+2] or str[i+1] == str[i+2]):
                return False
        return True
    return len(s) >= 3 and is_consecutive(s)
    
