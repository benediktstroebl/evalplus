
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
    # Create a set to store the distinct letters
    letters = set()
    for c in s:
        if c in letters:
            letters.remove(c)
        else:
            letters.add(c)
    return len(s) >= 3 and len(letters) == 3 and all(c in letters for c in s[::3])
