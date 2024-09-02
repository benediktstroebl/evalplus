
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    word1 = a.lower()
    for c in word1:
        word2 = b.lower()
        for i in range(len(word2)):
            # for each letter of the second word
            for j in range(len(word1)):
                # for each letter of the first word
                if word2[i] in word1[j:j+len(word2[i])] or word2[i] in word1[j-len(word2[i]):j] or word2[i] in word1[j:j+len(word2[i])]:
                    return True
    return False