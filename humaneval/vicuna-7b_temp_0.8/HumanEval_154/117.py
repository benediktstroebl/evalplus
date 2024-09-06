
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    # define a set to store the rotations of b
    rotations = set()
    for i in range(len(b)):
        rotations.add(b[i:i+1].upper() + b[i+1:len(b)] )
    
    for i in range(len(a)):
        # check if the second word or its rotations are in the first word
        for j in range(len(b)):
            if a[i:i+1].upper() == b[j:j+1].upper() or b[j:j+1].upper() in rotations:
                return True
    return False
