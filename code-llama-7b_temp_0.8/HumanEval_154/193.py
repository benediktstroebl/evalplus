
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if len(b)==0:
        return True
    if len(b)==1:
        return b in a

    if len(a)<len(b):
        return False

    ans = False
    for i in range(len(a)):
        if a[i:i+len(b)]==b:
            ans = True
            break
        temp = a[i:i+len(b)] + a[0:i]
        if temp==b:
            ans = True
            break

    return ans
