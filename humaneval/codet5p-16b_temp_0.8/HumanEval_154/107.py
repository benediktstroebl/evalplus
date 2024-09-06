
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """

    #make the first word a list and then use the list in each rotation
    lst_a = list(a)
    for i in range(len(a)):
        new_a = lst_a[-1:]+lst_a[:-1]
        if b in "".join(new_a):
            return True
    return False
    
