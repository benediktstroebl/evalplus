
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    # Slice the string in half (halfA + halfB)
    halfA, halfB = a[:len(a) // 2], a[len(a) // 2:]
    if a == halfB + halfA:
        return b in a
    return b in a or b in a[::-1]




    return True
