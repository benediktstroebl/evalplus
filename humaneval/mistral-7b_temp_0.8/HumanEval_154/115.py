
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """

    # pre-processing
    # 1. lowercase
    a = a.lower()
    b = b.lower()
    # 2. remove spaces
    a = a.replace(" ", "")
    b = b.replace(" ", "")
    # 3. add $ to both ends
    a = "$" + a + "$"
    b = "$" + b + "$"

    # make the list of rotations
    # a = list(a)
    # a.append(a.pop(0))

    # a = "".join(a)

    # check if b is in a
    # if b in a:
    #     return True
    # else:
    #     return False
    #
    # # for each element in a, check if b is in it
    # for i in a:
    #     if b in i:
    #         return True
    # return False


    # iterate through a and check if b is a substring
    # for i in a:
    #     if b in i:
    #         return
