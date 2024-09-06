
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    # create a dictionary of rotated words
    rotated_words = {word: word[::-1] for word in set(a)}

    # check if the second word or its rotations is a substring in the first word
    for r in rotated_words:
        if r in b:
            return True

    return False

