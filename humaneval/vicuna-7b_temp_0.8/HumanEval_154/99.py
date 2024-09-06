
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] == b[j] or a[i] == b[j]+ord(a[i])-ord('a') or b[j] == a[i]+ord(b[j])-ord(b[j])+1 or a[i:i+2] in b[j:j+2]:
            i += 1
        else:
            j += 1
    return j == len(b)