
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

    import re
    if len(s) < 3:
        return False
    else:
        s_list = re.split(r'(?<=[a-zA-Z0-9])',s)
        if len(s_list) == 1:
            return True
        else:
            count = 0
            for i in s_list:
                if i == i[::-1]:
                    count += 1
            if count == len(s_list):
                return True
            else:
                return False
            
