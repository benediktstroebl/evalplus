
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
    len_a = len(a)
    len_b = len(b)

    if len_a > len_b:
        for i in range(len_a - len_b + 1):
            if b == a[i:i+len_b] or b == a[i:i+len_b][::-1]:
                return True
    else:
        for i in range(len_b - len_a + 1):
            if a == b[i:i+len_a] or a == b[i:i+len_a][::-1]:
                return True

    return False
