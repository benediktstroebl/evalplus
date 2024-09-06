
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
    if len(s) < 3:
        return False
    arr = list(s)
    count = 0
    while count < len(arr) - 2:
        if arr[count] == arr[count + 1] or arr[count] == arr[count + 2] or arr[count + 1] == arr[count + 2]:
            return False
        count += 1
    return True

