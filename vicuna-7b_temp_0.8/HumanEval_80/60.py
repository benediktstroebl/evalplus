
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
    # To check if the length is at least 3
    if len(s) < 3:
        return False
    
    # To check if every 3 consecutive letters are distinct
    distinct_letters = set()
    for i in range(0, len(s), 3):
        distinct_letters.add(s[i])
        for j in range(i+1, len(s), 3):
            if s[j] == s[i]:
                distinct_letters.remove(s[i])
                break
    else:
        return True
    return False