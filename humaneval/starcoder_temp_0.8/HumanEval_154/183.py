
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    i = 0
    b = list(b)
    while i < len(b):
        if b[0] in a:
            if a.index(b[0]) + len(b) <= len(a):
                if b == a[a.index(b[0]):a.index(b[0]) + len(b)]:
                    return True
        b.insert(0, b.pop())
        i += 1

    return False
