
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """

    a_ = a.lower()
    b_ = b.lower()
    a_len = len(a_)
    b_len = len(b_)
    count = 0
    for i in range(a_len):
        for j in range(b_len):
            if a_[i] == b_[j]:
                count += 1
    return count == b_len
