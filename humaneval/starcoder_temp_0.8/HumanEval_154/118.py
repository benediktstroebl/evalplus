
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    #code here
    a_len = len(a)
    b_len = len(b)

    # if both words are of same length then simply do string comparison
    if a_len == b_len:
        return b in a
    elif b_len > a_len:
        return False

    # else find the period of rotation and check if the substring is present
    for i in range(a_len):
        if a[(i + b_len) % a_len] == b[0]:
            return b in a[(i + 1) % a_len:]

    return False

