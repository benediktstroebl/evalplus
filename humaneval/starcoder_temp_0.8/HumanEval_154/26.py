
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def cycpattern_check(self):
        return True if self.b in self.a or self.b in self.a[1:] or self.b in self.a[2:] else False
