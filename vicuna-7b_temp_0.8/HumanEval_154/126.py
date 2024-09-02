
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    ab = set(a)
    cd = set(b)
    abcd = sorted(ab) + sorted(cd)
    if len(ab) > len(cd):
        ab = sorted(ab)
        cd = sorted(cd)
    # len(ab) > len(cd)
    # abcd = sorted(ab) + sorted(cd)
    if len(ab) != len(cd):
        return False
    for ab_item in ab:
        if ab_item in cd or cd_item in ab_item:
            return True
    return False