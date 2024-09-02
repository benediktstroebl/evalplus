
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
    from collections import Counter

    def distinct_chars_in_a_string(s):
        counter = Counter(s)
        return all(c > 0 and len(counter) - c < 2 for c in counter.values())

    return len(s) >= 3 and distinct_chars_in_a_string(s
