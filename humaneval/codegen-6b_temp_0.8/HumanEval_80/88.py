
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
        return True

    # ###########################################
    # let's assume that we have a sorted string, I am not sure did I use the sorted string
    # ##################
    # I assume that when I am using it here, I am creating a set, which means that I assume that
    # I am using DUPLICATE CHECKING
    # ##################
    # It is better to test if the length is at least 3, because if it is less than 3, it will never
    # be a string of two consecutive letters
    prev_letter = set(s[:3])
    for i in range(3, len(s), 3):
        if len(prev_letter) < 3:
            return False
        substr = s[i:i+3]
        curr_letter = set(substr)
        if len(curr_letter - prev_letter) != 1:
            return False
        prev_letter = curr_letter
    return True

