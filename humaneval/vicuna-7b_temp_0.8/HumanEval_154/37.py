
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    for i in range(len(b)):
        if b[i] == 'x':
            for j in range(i+1, len(b)):
                if b[j] == 'x':
                    if a[j-i-1] == b[j-1]:
                        return True
    return False