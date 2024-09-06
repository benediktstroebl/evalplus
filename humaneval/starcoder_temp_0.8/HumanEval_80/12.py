
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
    a = s
    b = ""
    while a!= b:
        a = s
        b = ""
        for i in range(len(a)-2):
            b += a[i]
            if b in a[i+1:] and b!= "":
                return False
            b = ""
    return True
