
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if a.endswith(b) or b.endswith(a):
        return True
    for i in range(1, len(a)):
        for j in range(1, len(b)):
            c = a[i:j]
            if c in b:
                if any(b.startswith(c[k:]) for k in range(1, len(c))) or \
                   any(b.endswith(c[k:]) for k in range(1, len(c))) or \
                   any(c.endswith(b[k:]) for k in range(1, len(c))) or \
                   any(c.startswith(b[k:]) for k in range(1, len(b))) or \
                   any(c.endswith(b[k:]) for k in range(1, len(b))):
                return True
    return False