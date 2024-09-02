
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    word2 = a
    word1 = b
    # a=word1
    # b=word2
    #print(word2)
    #print(word1)
    if word2 in word1:
        return True
    else:
        while word2 not in word1:
            word2 = word2[1:]+word2[0]
        return True

