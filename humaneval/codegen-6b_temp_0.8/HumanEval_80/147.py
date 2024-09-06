
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
    # if s is of length 1 or less, then it is not happy
    if len(s) <= 2:
        return False

    # create a list of the first 3 characters
    abc = [s[i] for i in range(0, 3)]

    # if all three characters are same, then string is happy
    if abc[0] == abc[1] == abc[2]:
        return True

    # else, if there is only one character, then string is not happy
    if len(s) == 1:
        return False

    # else, if there are repeating characters, then there is no happy string
    for i in range(0, len(s) - 2):
        if s[i] == s[i+1] == s[i+2]:
            return False

    # else, we have a happy string
    return True

