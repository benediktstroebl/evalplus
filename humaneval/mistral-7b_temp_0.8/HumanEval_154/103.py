
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """

    firstword = list(a)
    secondword = list(b)

    if len(firstword)!=len(secondword):
        return False

    for i in range(len(firstword)):
        if firstword[i]!=secondword[i]:
            return False
    return True


