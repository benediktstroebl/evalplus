
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

    current_number = 0
    for i in range(0,len(s)):
        current_number += ord(s[i])**2
    if len(s) <= 2:
        return False
    return current_number == ord(s[0])**2 + ord(s[1])**2 + ord(s[2])**2 + ord(s[3])**2
