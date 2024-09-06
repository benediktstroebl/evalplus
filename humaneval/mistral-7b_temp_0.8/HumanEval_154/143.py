
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    first_word = a
    second_word = b
    if second_word in first_word:
        return True
    elif len(second_word) != len(first_word):
        return False
    else:
        for i in range(len(first_word)):
            if first_word[i:]+first_word[0:i] == second_word:
                return True
        return False
