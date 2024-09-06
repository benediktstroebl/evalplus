
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """

    #checks if b is a substring in a
    if b in a:
        return True

    #rotates b to create more possibilities
    else:
        temp = b
        result = False
        while temp != a:
            temp = temp[1:] + temp[0]
            if temp in a:
                result = True
                break

        return result


