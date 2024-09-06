
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    #first we need to find all the rotations of the string, e.g if string is "abc" then all rotations will be
    #"abc","bca","cab"
    #so we use rotations function.

    rotations = rotations_of_string(b)
    #now we check if any rotation is present in the string, if yes then return true, if not then false
    for rotation in rotations:
        if rotation in a:
            return True
    return False
