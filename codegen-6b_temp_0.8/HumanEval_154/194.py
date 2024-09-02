
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    # create a hash table for each word and check if its substring
    # works on each rotation of the word
    substr_hash = {}
    for i in range(1, len(a)):
        substr_hash[a[i:]] = True
        substr_hash[a[:-i]] = True
    return substr_hash.get(b, False)

