
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if len(a) >= len(b):
        for i in range(len(a)):
            for j in range(i, len(a)):
                if (len(a[i:j]) == len(b)):
                    print(a[i:j])
                    if a[i:j].find(b) >= 0:
                        return True
        return False
    else:
        return False
