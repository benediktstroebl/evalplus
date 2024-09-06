
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    word_b = b
    if len(word_b) > len(a):
        return False

    if word_b == a[:len(word_b)]:
        return True

    word_b = word_b + word_b
    num_rotations = len(a) // len(word_b)
    for i in range(num_rotations):
        if word_b[i * len(word_b): (i * len(word_b) + len(word_b))] == a:
            return True
    return False
