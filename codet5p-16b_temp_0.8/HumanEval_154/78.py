
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """

    a=a.lower()
    b=b.lower()
    list_a = list(a)
    list_b = list(b)
    if len(list_b) <= len(list_a):
        for i in range(len(list_a)):
            if list_a[i:len(list_b)+i] == list_b:
                return True
        return False
    else:
        for i in range(len(list_b)):
            if list_b[i:len(list_a)+i] == list_a:
                return True
        return False

