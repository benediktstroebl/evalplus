
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    first = list(a)
    second = list(b)

    if len(second) > len(first):
        return False
    for i in range(len(first)):
        if first[i] == second[i % len(second)]:
            continue
        else:
            return False

    
