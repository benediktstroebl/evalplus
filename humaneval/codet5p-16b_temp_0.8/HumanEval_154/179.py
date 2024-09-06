
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """

    if a == b:
        return True
    else:
        a_len = len(a)
        b_len = len(b)
        rotations_b = set()
        for i in range(b_len):
            rotations_b.add(b[i:]+b[:i])

        for i in range(a_len):
            if a[i:]+a[:i] in rotations_b:
                return True
            else:
                continue
        return False
        
