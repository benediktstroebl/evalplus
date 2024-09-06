
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if(a == b):
        return True
    if (len(a) < len(b)):
        return False
    a_hash = {}
    for x in a:
        if x in a_hash:
            a_hash[x] += 1
        else:
            a_hash[x] = 1
    # print(a_hash)
    b_hash = {}
    for x in b:
        if x in b_hash:
            b_hash[x] += 1
        else:
            b_hash[x] = 1
    # print(b_hash)
    if (a_hash == b_hash):
        return True
    for i in range(len(b)):
        rotated_b = b[i:] + b[:i]
        if(rotated_b in a):
            return True
    return False
