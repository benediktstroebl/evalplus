
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """

    a_words = a
    a_words_len = len(a)

    b_words = b
    b_words_len = len(b)

    if a_words_len == b_words_len:
        for i in range(0, a_words_len):
            if b_words == a_words:
                return True
            a_words = a_words[1:] + a_words[0]
    else:
        return False
