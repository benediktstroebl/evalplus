
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    def find_rotation(a, b):
        # Your code goes here
        if len(b) < len(a):
            return False
        if b in a:
            return True
        for i in range(len(a)):
            s = a[i:]+a[:i]
            if s == b:
                return True
        return False
    return find_rotation(a,b) or find_rotation(b,a)



