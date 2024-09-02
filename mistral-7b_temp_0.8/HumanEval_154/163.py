
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    # creating a map of count of each alphabet in the first word
    first_word_map = {}
    for i in a:
        if i in first_word_map:
            first_word_map[i] += 1
        else:
            first_word_map[i] = 1
    # creating a map of count of each alphabet in the second word
    second_word_map = {}
    for i in b:
        if i in second_word_map:
            second_word_map[i] += 1
        else:
            second_word_map[i] = 1

    # if the two word maps are not equal then return False
    if first_word_map != second_word_map:
        return False

    # if the second word or its rotation is a substring of the first word then return True
    if b in a or b in reversed(a):
        return True
    else:
        return False
