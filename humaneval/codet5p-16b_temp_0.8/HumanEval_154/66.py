
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """

    
    def _rotations(a):
        rotations = [a[:i] + a[i:][::-1] for i in range(len(a))]
        rotations.append(a[::-1])
        return rotations

    for i in _rotations(a):
        if i in b or b in i:
            return True
    return False
    
    
