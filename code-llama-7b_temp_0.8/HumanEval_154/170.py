
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """

    a_set = set(a)
    b_set = set(b)

    if len(a_set.difference(b_set)) > 0:
        return False

    for i in range(len(b)):
        for j in range(len(b) + 1):
            if j <= len(b):
                if b[i:] + b[:i] == a[j:j+len(b)] or b == a:
                    return True
            else:
                if b + b[i:] == a[j:j+len(b)]:
                    return True
    return False


