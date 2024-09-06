
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    # Write your logic here
    # return your answer

    word = a
    print(word)
    l=len(word)
    print(l)
    for i in range(0,l):
        if word[i] == word[0]:
            print(word[i],word[0])
        else:
            return False
    for i in range(0,l):
        if word[-i] == word[-1]:
            print(word[-i],word[-1])
        else:
            return False

    word2 = b
    l2=len(word2)
    print(word2)
    print(l2)
    for i in range(0,l2):
        if word2[i] == word2[0]:
            print(word2[i],word2[0])
        else:
            return False
    for i in range(0,l2):
        if word2[-i] == word2[-1]:
            print(word2[-i],word2[-1])
        else:
            return False
    return True
