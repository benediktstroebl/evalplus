
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    # 1.
    # if len(a) > len(b):
    #     return False

    # 2.
    # for i in range(len(a)):
    #     if a[:i] + b in a:
    #         return True
    # return False

    # 3.
    # import itertools
    # # a = list(a)
    # # b = list(b)
    # for x in itertools.permutations(b):
    #     if x in a:
    #         return True
    # return False



    # 4.
    # import itertools
    # for x in itertools.permutations(b):
    #     for i in range(len(a)-len(b)):
    #         if x in a[i:i+len(b)]:
    #             return True
    # return False

    # 5.
    # import itertools
    # if len(b) > len(a):
    #     return False
    # for i in range(len(a)):
