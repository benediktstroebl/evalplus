
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
    def is_distinct(i, count, letters):
        if count >= 3:
            return letters[i] != letters[i - 1] or letters[i] != letters[i - 2]
        return False
    
    letters = set()
    for i in range(len(s)):
        if i >= 3:
            letters.remove(s[i - 2])
        letters.add(s[i])
        if len(letters) > 2:
            return False
    return True

assert(is_happy('a') == False)
assert(is_happy('aa') == False)
assert(is_happy('abcd') == True)
assert(is_happy('aabb') == False)
assert(is_happy('adb') == True)
assert(is_happy('xyy') == False)
