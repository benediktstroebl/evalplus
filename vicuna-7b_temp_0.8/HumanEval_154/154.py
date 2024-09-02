
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    # define list of rotated word
    rotated = [x + y for x, y in zip(a, b)]
    
    # check if any of rotated words is a substring of first word
    for rotated_word in rotated:
        if rotated_word in a:
            return True
    return False