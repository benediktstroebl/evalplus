
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """

    str1 = a
    str2 = b
    str2_len = len(str2)

    if str2_len <= len(str1):

        for index in range(0, str2_len):
            if (str2 == str1[index:index + str2_len]) or (str2 == str1[index + 1:index + str2_len + 1]):
                return True
        return False
    return False
