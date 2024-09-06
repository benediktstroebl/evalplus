
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
    def count_distinct_chars(s):
        count = {}
        for c in s:
            if c in count:
                count[c] += 1
            else:
                count[c] = 1
        return count
    
    def check_happy(s):
        if len(s) < 3:
            return False
        count = count_distinct_chars(s)
        for i in range(0, len(s), 3):
            if count[s[i]] == 1:
                return False
        return True
    
    return check_happy(s)
