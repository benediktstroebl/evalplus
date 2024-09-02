
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
    n = len(s)
    if n < 3:
        return False
    for i in range(n-1, -1, -1):
        curr_letters = s[i:i+3]
        distinct = True
        for j in range(3):
            if curr_letters[j] == curr_letters[j+1]:
                distinct = False
                break
        if distinct:
            return True
    return False
