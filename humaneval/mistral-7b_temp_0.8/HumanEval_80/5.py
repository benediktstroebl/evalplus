
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
    return len(s) >= 3 and (len(s) - 2) % 2 == 0 and len(set(s[:3])) == 3
    # https://stackoverflow.com/questions/10236614/get-all-n-length-combinations-from-a-string-in-python/10236892#10236892
