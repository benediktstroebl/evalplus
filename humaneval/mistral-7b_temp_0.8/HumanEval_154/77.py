
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    substrings=[]
    for i in range(len(a)):
        substrings.append(a[i:len(a)])
    for i in range(len(b)):
        for j in substrings:
            if j==b:
                return True
    return False
