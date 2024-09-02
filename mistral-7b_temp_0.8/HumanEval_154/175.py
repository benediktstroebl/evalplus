
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if not a or not b:
        return False

    word1_len = len(a)
    word2_len = len(b)

    for i in range(word1_len):
        for j in range(word2_len):
            if word2_len % j != 0:
                continue
            else:
                jth_sub = b[j:] + b[:j]
                if a.find(jth_sub) != -1:
                    return True

    return False

































































































































