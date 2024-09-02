
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """

    firstword = a.lower()
    secondword = b.lower()
    if len(firstword) < len(secondword) or len(firstword) == 0:
        return False

    if secondword in firstword:
        return True

    if len(firstword) < len(secondword):
        return False

    i = 0
    while i < len(secondword):
        j = 0
        while j < len(secondword):
            if firstword[i + j] != secondword[j]:
                break
            j += 1
        i += 1
    return j == len(secondword)
