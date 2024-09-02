
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
    if s[:3]==s[3:]:
        return s[:3]
    s = s.replace(" ","")
    arr = [i for i in s if i not in "1234567890"]
    if len(arr) >= 3:
        arr1 = arr[:3]
        for i in range(1,len(arr1)):
            if arr1[i-1] == arr1[i]:
                return False
        return True
    else:
        return False
