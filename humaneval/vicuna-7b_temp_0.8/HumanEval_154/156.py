
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    d = ""
    for i in range(len(a)):
        d = d + a[i]
    for i in range(len(b)):
        if b[i:len(b)] in d or b[i:len(b)] == d[::-1]:
            return True
    return False

a = input().split()
b = input().split()
