
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    def all_rotations(a):
        return [a+a[0:1], a+a[1:2], a+a[2:3], a+a[3:4], a+a[4:5], a+a[5:6], a+a[6:7], a+a[7:8], a+a[8:9]]

    def is_rotation(a, b):
        if a==b:
            return True
        elif len(a)!=len(b):
            return False
        else:
            if a[0:len(b)] == b:
                return True
            else:
                return False


    if len(a)!=len(b):
        return False
    if is_rotation(a,b):
        return True

    for i in range(1,len(a)):
        rot_a=all_rotations(a[i:len(a)])
        for rot in rot_a:
            if is_rotation(rot,b):
                return True
        return False

    return
