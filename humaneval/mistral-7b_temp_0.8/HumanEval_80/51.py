
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
    import re
    try:
        x =  re.search(r'[a-zA-Z]{3}', s).group()
    except AttributeError:
        return False
    return all(x != x[i:i+3] for i in range(len(x)-2))

    return False





