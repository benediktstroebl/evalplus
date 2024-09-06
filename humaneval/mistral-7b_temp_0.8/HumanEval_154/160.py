
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

    # in case of second word is the substring in first word
    if second_word in first_word:
        return True

    # in case of second word is the substring in first word after it rotates
    for i in range(len(second_word)):
        if first_word.find(second_word[i:] + second_word[:i]) != -1:
            return True

    return False
