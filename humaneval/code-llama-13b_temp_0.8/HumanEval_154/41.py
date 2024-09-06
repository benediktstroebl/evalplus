
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    # check if the second word is in the first word
    # if yes return True
    # if not check the other rotations of the second word
    # if found return True
    # else return False
    # Only 1 liners please :)
    return b in a or any(a.index(b[i:] + b[:i]) >= 0 for i in range(len(b)))




