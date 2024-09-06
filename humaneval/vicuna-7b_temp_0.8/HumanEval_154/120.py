
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    for i in range(len(a)):
        for j in range(len(b)):
            if (j+1) % 4 == 1 and b[j] == a[i] or (j+1) % 4 == 2 and b[j] == a[i+1] or (j+1) % 4 == 3 and b[j] == a[i+2] or b[j] == a[i] or (j+1) % 4 == 0 and b[j] == a[i+3]:
                return True
    return False
