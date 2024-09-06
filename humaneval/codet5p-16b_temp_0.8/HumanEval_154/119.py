
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """

    word1 = a.lower()
    word2 = b.lower()
    len_w1 = len(word1)
    len_w2 = len(word2)
    if len_w1 < len_w2:
        return False
    else:
        for i in range(len_w1-len_w2):
            if word1[i:i+len_w2] == word2 or word2 in word1:
                return True
            else:
                return False
                


