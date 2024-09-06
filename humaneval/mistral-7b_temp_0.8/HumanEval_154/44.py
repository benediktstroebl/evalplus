
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    print("Check if the word {} or any of its rotations is present in the word {}".format(b,a))

    if len(a) == 0 or len(b) == 0:
        return False

    for i in range(len(b)):
        if b[i:] + b[:i] in a:
            return True

    return False
