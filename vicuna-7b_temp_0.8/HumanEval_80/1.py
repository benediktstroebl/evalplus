
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
    # if len(s) < 3:
    #     return False
    if len(s) < 3:
        return False

    distinct_chars = set(s)
    for i in range(1, len(s)):
        for j in range(i+1, len(s)):
            for k in range(j+1, len(s)):
                if distinct_chars.intersection(set(s[:i+1])).intersection(set(s[i+1:j+1])).intersection(set(s[j+1:k+1])) == set():
                    distinct_chars.discard(s[i+1])
                    distinct_chars.discard(s[j+1])
                    distinct_chars.discard(s[k+1])
                    return True
    return False