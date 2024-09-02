
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    #check if b in a
    # b in a
    # b[0] in a
    # a[b[0] in a
    # b[0] in a[0:i]
    # b in a[0:i]

    # b[1] in a[0:i]
    # b in a[0:i]
    # b[2] in a[0:i]
    # b in a[0:i]
    # b[3] in a[0:i]
    # b in a[0:i]
    # b[4] in a[0:i]
    # b in a[0:i]
    # b[5] in a[0:i]
    # b in a[0:i]


    # or 

    # if b in a[0:i]
    # return True
    # if b in a[0:i+1]
    # return True
    # if b in a[0:i+2]
    # return True
    # if b in a[0:i+3]
    # return True
    # return False

    # or

    # if b not in a[0:i]
    # return False

    # if b not in a[0:i+1]
    # return False

    # if b not in a[0:i+2]
    # return False

    # if b not in a[0:i+3]
    # return False

    # return True

    # or

    # if b in a[0:i]
    # return True

    # if b in a[0:i+1]
    # return True

    # if b in a[0:i+2]
    # return True

    # if b in a[0:i+3]
    # return True

    # return False

    # or

    # return not(b not in a[0:i])

    # or

    # return b in a[0:i]
    # return b in a[0:i+1]
    # return b in
