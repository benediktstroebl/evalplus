
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    # for index, value in enumerate(a):
    #     b_rot = b[index:] + b[0:index]
    #     # print(b_rot)
    #     # if b in a:
    #     if b_rot in a:
    #         return True
    # return False
    a = list(a)
    b = list(b)
    # print(a)
    # print(b)
    a_rot = list(a)
    for index, value in enumerate(a):
        a_rot.append(a_rot.pop(0))
        # print(a_rot)
        if a_rot == b:
            return True
    return False

