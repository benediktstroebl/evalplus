
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
    seen = []
    while True:
        seen.append(s)
        if len(s) < 3:
            return False
        letters = [i for i in s]
        for i in range(0, len(letters) - 3):
            if letters[i] == letters[i + 1] and letters[i] == letters[i + 2] and letters[i] == letters[i + 3]:
                return False
        if s in seen:
            return False
        else:
            s = ''.join(letters)
        
        
