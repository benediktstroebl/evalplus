
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    a = a.replace(" ", "")
    b = b.replace(" ", "")
    a_length = len(a)
    b_length = len(b)
    if a_length != b_length:
        return False
    if a_length == 0:
        return True
    for i in range(0, b_length):
        if b in a:
            return True
        new_string = b[i:] + b[0:i]
        if new_string in a:
            return True
    return False
