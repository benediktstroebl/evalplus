
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    def check(str1,str2):
        for i in range(len(str1)):
            if str1[i:i+len(str2)] == str2:
                return True
        return False

    str1 = a
    str2 = b
    if len(str2) > len(str1):
        return False
    else:
        if check(str1,str2):
            return True
        else:
            return False
