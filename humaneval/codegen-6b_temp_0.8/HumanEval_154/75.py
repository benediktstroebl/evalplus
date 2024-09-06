
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    def check(word1, word2):
        l1 = len(word1)
        l2 = len(word2)

        if l1 > l2:
            return False
        for i in range(l1):
            if word1[i:i+l2] == word2:
                return True
        else:
            return False

    for l in range(len(a)):
        if check(a, a[l:] + a[:l]):
            return True

    return False
