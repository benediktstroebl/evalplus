
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
    happy_char = False
    happy_len = 3
    for index, char in enumerate(s):
        if index == 0:
            happy_char = char == s[index+1] and char == s[index+2]
        else:
            happy_char = happy_char and char == s[index-1] and char == s[index+1]
        if happy_char:
            happy_len -= 1
            if happy_len <= 0:
                return True
    return happy_char

