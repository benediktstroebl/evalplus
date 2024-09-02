
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    def cycpattern_check_rotate(w,sub):
        result = ''
        for i in xrange(len(w)):
            result = w[i:] + result + w[:i]
        return result.find(sub) != -1

    def cycpattern_check_next(w,sub):
        l = len(sub)
        if w[l:] + w[:l] == sub:
            return True
        return False

    l1 = len(a)
    l2 = len(b)

    if l1 < l2:
        a,b = b,a
    for i in xrange(l1-l2):
        if cycpattern_check_rotate(a,b) or cycpattern_check_next(a,b):
            return True
    return False
