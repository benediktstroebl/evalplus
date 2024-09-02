
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
    import collections
    count = collections.defaultdict(int)
    for letter in s[:len(s) - 1]:
        count[letter] += 1
    return count[s[-1]] >= 3 and all(count[letter] >= count[letter + 1] for letter in count)

