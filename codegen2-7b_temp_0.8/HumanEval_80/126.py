
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
    def is_happy(s):
        index = 0
        while index < len(s)-2:
            char = s[index]
            index += 1
            if char == s[index]:
                return False
            if index == len(s)-1:
                return True
            else:
                if char == s[index] and char == s[index+1] and char == s[index+2]:
                    index += 2
                else:
                    return False
        return True
    return is_happy(s
