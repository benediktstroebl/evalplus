
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """

    if (a == "") or (b == ""):
        return False

    elif len(a) < len(b):
        return False

    elif len(a) == len(b):

        for x in range(len(b)):

            if b == a[x:] + a[:x]:
                return True
            else:
                return False

    else:

        for x in range(len(b)):

            if b == a[x:] + a[:x]:
                return True

            if b == a[-x:] + a[:-x]:
                return True
            else:
                return False



