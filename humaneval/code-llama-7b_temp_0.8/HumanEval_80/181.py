
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

    # we use 3 pointers, one to the end of the string and the other two at positions 1 and 2
    # if the pointer at position 1 and 2 are equal to the pointer at the end of the string, the string is not happy
    # else we increment the pointer 2 and the pointer at position 1 and check again
    # if the pointer at position 2 is at the end of the string, we increment the pointer 1
    # and we reset the pointer at position 2 to the pointer at position 1
    # then we increment the pointer at position 1
    # if we reach the end of the string, the string is not happy

    end = len(s) - 1
    one, two = 1, 2
    while True:
        if s[one] == s[end] and s[two] == s[end]:
            return False
        if two == end:
            if one == end:
                return False
            one += 1
            two = one + 1
            continue
        two += 1
        if two == end:
            one += 1
            two = one + 1
    return True

