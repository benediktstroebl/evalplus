
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    for x in b:
        for i in range(len(a)):
            if x in a[i:] or x == a[i:].rot(1) or x == a[i:].rot(2) or x == a[i:].rot(3) or x == a[i:].rot(4) or x == a[i:].rot(5) or x == a[i:].rot(6) or x == a[i:].rot(7) or x == a[i:].rot(8) or x == a[i:].rot(9) or x == a[i:].rot(10) or x == a[i:].rot(11) or x == a[i:].rot(12) or x == a[i:].rot(13) or x == a[i:].rot(14) or x == a[i:].rot(15) or x == a[i:].rot(16) or x == a[i:].rot(17) or x == a[i:].rot(18) or x == a[i:].rot(19) or x == a[i:].rot(20) or x == a[i:].rot(21) or x == a[i:].rot(22) or x == a[i:].rot(23) or x == a[i:].rot(24) or x == a[i:].rot(25) or x == a[i:].rot(26) or x == a[i:].rot(27) or x == a[i:].rot(28) or x == a[i:].rot(29) or x == a[i:].rot(30) or x == a[i:].rot(31) or x == a[i:].rot(32) or x == a[i:].rot(33) or x == a[i:].rot(34) or x == a[i:].rot(35) or x == a[i:].rot(36) or x == a[i:].rot(37) or x == a[i:].rot(38) or
