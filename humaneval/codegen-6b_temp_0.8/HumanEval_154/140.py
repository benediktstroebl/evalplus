
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    length_a = len(a)
    length_b = len(b)
    if length_a == length_b:
        return b in a
    else:
        for i in range(length_a):
            if b[i:] == a[length_a-length_b+i:]:
                return True
            elif a[i:] == b[length_b-length_a+i:]:
                return True
        return False
