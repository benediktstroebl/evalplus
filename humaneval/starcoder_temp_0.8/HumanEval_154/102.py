
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
    for i in range(len(first_word)):
        for j in range(i+1, len(first_word)+1):
            if first_word[i:j] == second_word or first_word[i:j] == second_word[::-1]:
                return True
    return False
