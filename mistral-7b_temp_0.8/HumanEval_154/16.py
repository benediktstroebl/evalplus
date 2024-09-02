
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    # convert the two strings to lowercase
    word1 = a.lower()
    word2 = b.lower()

    # check if the second word is a substring in the first word
    if word2 in word1:
        return True

    # rotate the second word until it becomes a substring in the first word
    for i in range(len(word2)):
        if word2[i:] + word2[:i] in word1:
            return True

    # if none of the rotations of the second word is a substring in the first word, return False
    return False

