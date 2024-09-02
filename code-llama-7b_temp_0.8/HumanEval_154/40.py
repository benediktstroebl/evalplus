
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if len(a) == 0 or len(b) == 0:
        return False
    
    l1 = len(a)
    l2 = len(b)
    
    if l1 < l2:
        return False

    if a.find(b) != -1:
        return True

    for i in range(l1):
        rotated_str = get_rotated_str(a, i)
        if b in rotated_str:
            return True

    return False
