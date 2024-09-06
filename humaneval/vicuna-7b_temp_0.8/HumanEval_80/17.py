
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
    # Find all the pairs of consecutive letters
    # and check if all the pairs are distinct
    pairs = [(i, i+1) for i in range(len(s)-1)]
    distinct_pairs = []
    for i, j in pairs:
        if s[i] != s[j+1]:
            distinct_pairs.append(i)
    return len(distinct_pairs) >= 3
