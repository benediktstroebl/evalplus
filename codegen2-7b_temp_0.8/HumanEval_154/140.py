
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    def cnt_in_word(word,cnt):
        if cnt == 0:
            return True
        if word[0] in word:
            return cnt_in_word(word[1:],cnt-1)
        return cnt_in_word(word[1:],cnt)
    return cnt_in_word(b,len(a))
