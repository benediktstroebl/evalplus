
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    first_word=a
    second_word=b
    first_word=first_word.lower()
    second_word=second_word.lower()
    if(second_word in first_word):
        return True
    else:
        if(second_word in second_word):
            return True
        for i in range(len(second_word)):
            if(second_word[i] in first_word):
                return True
        return
