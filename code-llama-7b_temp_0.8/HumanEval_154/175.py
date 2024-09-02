
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if len(a) > len(b):
        return False

    a_letter = [c for c in a]
    b_letter = [c for c in b]

    if a_letter == b_letter:
        return True

    for i in range(len(b)):
        if b_letter == a_letter:
            return True
        a_letter.append(a_letter.pop(0))

    return False
