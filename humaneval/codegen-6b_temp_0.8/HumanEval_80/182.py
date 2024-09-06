
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
    # check if s is < 3
    if len(s) < 3:
        return False

    # initialize a list to hold consecutive 3 chars
    l = []

    # loop to check each consecutive 3 chars
    for i in range(len(s)-2):
        # is the consecutive 3 char different?
        if s[i] != s[i+1] and s[i+1] != s[i+2]:
            # append to list
            l.append(s[i])

    # check if there's a char that's not in the list
    if len(l) < 1:
        return False

    # if no consecutive 3 char, check if list is of length 2 or 3
    elif len(l) < 3:
        return True

    # if list of length 3, check if all 3 consecutive chars are different
    else:
        for i in range(3):
            if l[i] == l[i+1]:
                return False
        return True
