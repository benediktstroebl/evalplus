
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
    count = Counter()
    for i in xrange(len(s)):
        for j in xrange(i+1, len(s)):
            if count[s[i]] > 0:
                count[s[i]] -= 1
            if count[s[j]] > 0:
                count[s[j]] -= 1
            if count[s[i]] == count[s[j]]:
                count[s[i]] += 1
    return count