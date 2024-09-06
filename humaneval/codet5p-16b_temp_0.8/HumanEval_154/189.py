
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """

    if len(a)<len(b):
        return False
    else:
        a_list = []
        b_list = []
        for i in range(len(a)):
            a_list.append(a[i])
            b_list.append(b[i])

        a_list.reverse()
        b_list.reverse()
        a_list.append(a[0])
        b_list.append(b[0])
        for i in range(len(a)):
            if b_list[i] in a_list:
                return True

        return False



