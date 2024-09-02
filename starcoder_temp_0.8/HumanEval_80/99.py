
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
    # initialize variables
    s_len = len(s)
    seen_values = []
    seen_values_length = 0
    # check if string is less than 3 characters
    if s_len <= 2:
        return False
    # get every three characters in the string
    for i in range(0, s_len - 2):
        value = s[i:i + 3]
        # if the value is already seen, return False
        if value in seen_values:
            return False
        # else, add value to seen_values list
        else:
            seen_values.append(value)
    # return True
    return True

