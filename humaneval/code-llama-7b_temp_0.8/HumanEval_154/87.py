
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """

    # first word
    fw = a
    # second word
    sw = b

    # list of rotated words
    rotaw = []

    # length of first word
    l = len(fw)

    # 
    for i in range(l):
        # rotating words
        fw = fw[-1] + fw[:-1]
        # 
        rotaw.append(fw)
    # checking for substring
    for i in rotaw:
        if i in sw:
            return True
    return False
