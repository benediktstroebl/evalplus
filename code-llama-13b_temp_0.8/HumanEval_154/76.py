
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    alist = []
    # print('a = {}'.format(a))
    # print('b = {}'.format(b))
    for i in range(len(a)):
        # print('i = {}'.format(i))
        # print('a[i:] = {}'.format(a[i:]))
        # print('a[:i] = {}'.format(a[:i]))
        # print('a[i:]+a[:i] = {}'.format(a[i:]+a[:i]))
        if b in a[i:]+a[:i]:
            return True
    return False

