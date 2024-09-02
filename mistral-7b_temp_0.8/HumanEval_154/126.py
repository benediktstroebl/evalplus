
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    str1 = a.lower()
    str2 = b.lower()

    if len(str1) < len(str2):
        str2, str1 = str1, str2

    for i in range(len(str2)):
        if str1.find(str2[i:]) != -1:
            return True

    return False

