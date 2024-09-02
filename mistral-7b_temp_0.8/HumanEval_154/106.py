
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    # using a dictionary to store all rotations of the second word
    dict={}
    for i in range(len(b)):
        dict[b[i:]+b[:i]]=1

    # checking if any of the rotations of b are present in a
    for i in range(len(a)):
        if a[i:]+a[:i] in dict:
            return True
    return False



