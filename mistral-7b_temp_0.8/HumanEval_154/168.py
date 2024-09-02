
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    word1 = a.lower().split('')
    word2 = b.lower().split('')
    if (word2 == word1[-len(word2):]):
        return True
    elif (word2 == word1[-len(word2):] + word1[:-len(word2)]):
        return True
    else:
        return False
