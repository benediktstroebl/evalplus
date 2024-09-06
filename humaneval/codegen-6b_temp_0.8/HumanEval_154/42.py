
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    print(a,b)
    if a == b:
        return True
    if len(a) == len(b) == 1:
        return False
    if set(a) & set(b):
        return True
    if list(a) == list(b) or list(a) == list(b)[-1::-1]:
        return True
    elif list(a) == list(b)[-1::-1]:
        return True
    elif list(b) == list(b)[-1::-1]:
        return True
    elif list(a) == list(b)[-2::-1]:
        return True
    elif list(b) == list(b)[-2::-1]:
        return True
    elif list(a) == list(b)[-3::-1]:
        return True
    elif list(b) == list(b)[-3::-1]:
        return True
    return False
