
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
    # check if length of s is greater than or equal to 3
    if len(s) < 3:
        return False
    
    # check if every 3 consecutive letters are distinct
    distinct_letters = False
    for i in range(1, len(s)):
        curr_letter = s[i]
        next_letter = s[i+1]
        if (curr_letter == next_letter) or (curr_letter == s[i-1]):
            continue
        distinct_letters = True
        break
    if not distinct_letters:
        return False
    else:
        return True
