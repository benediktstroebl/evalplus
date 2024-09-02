
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    first_word = a.lower()
    second_word = b.lower()

    if first_word == second_word:
        return True
    elif len(second_word) > len(first_word):
        return False
    else:
        return cycpattern_check(second_word, first_word[:len(second_word)])
