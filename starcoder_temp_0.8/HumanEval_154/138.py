
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    a = a.lower()
    b = b.lower()
    a_length = len(a)
    b_length = len(b)
    #check if the length of b is smaller than the length of a
    if b_length >= a_length:
        return False
    b_in_a = a.find(b)
    b_in_a_rev = a.find(b[::-1])
    if b_in_a_rev > b_in_a:
        return True
    return False
