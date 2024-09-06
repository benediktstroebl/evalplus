
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    #pattern = abcd
    #check = abd
    #output = True

    #pattern = hello
    #check = ell
    #output = True

    #pattern = whassup
    #check = psus
    #output = False

    #pattern = abab
    #check = baa
    #output = True

    #pattern = efef
    #check = eeff
    #output = False

    #pattern = himenss
    #check = simen
    #output = True
    pattern = a
    check = b
    if len(check) > len(pattern):
        return False
    for i in range(len(check)):
        if pattern.startswith(check):
            return True
        pattern = pattern[1:]
    return False
