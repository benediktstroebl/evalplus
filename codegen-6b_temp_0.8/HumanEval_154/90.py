
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    def check(a,b):
        for x in range(1,len(b)+1):
            if b[:x] in a:
                return True
        return False

    def check_rotate(a,b):
        for x in range(len(b)):
            if b[x:]+b[:x] == a:
                return True
        return False

    if check(a,b) or check_rotate(a,b):
        return True
    else:
        return False
