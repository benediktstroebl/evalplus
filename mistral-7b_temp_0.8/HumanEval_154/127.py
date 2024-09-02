
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """

    def rotation(s):
        i=0
        new_str=[]
        while i < len(s):
            new_str.append(s[i])
            i+=1
        return ''.join(new_str)

    for i in range(len(a)):
        if b in a[i:]:
            return True
        if rotation(b) in a[i:]:
            return True

    return False
