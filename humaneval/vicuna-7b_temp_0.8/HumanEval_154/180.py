
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    m,n = len(a),len(b)
    a_rot = "".join([b[i:i+len(a)] for i in range(0,n,len(a))])
    b_rot = "".join([a[i:i+len(b)] for i in range(0,m,len(b))])
    if a_rot in b or b_rot in a:
        return True
    else:
        return False
