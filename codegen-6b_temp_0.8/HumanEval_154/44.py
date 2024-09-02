
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
    first_len = len(first_word)
    first_word = first_word.lower()
    second_word = second_word.lower()
    second_word = second_word[0:len(second_word)] + second_word[0:len(second_word) - 1]
    if second_word in first_word:
        return True
    for i in range(first_len):
        first_word = first_word[1:] + first_word[0]
        if second_word in first_word:
            return True


    return False


