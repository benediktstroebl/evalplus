
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
    # different helper function:
    # 1. split string into list of characters
    # 2. check for consecutive letters
    # 3. return true or false
    def is_consecutive(i, j):
        return i == j + 1

    if len(s) < 3:
        return False

    chars = []
    for c in s:
        chars.append(c)

    occurrences = {}

    for i, c in enumerate(chars):
        if occurrences.get(c):
            occurrences[c] += 1
        else:
            occurrences[c] = 1

    for v in occurrences.values():
        if v != 1:
            return False

    return True
