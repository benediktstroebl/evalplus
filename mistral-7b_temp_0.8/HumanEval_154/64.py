
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    def rotate_word(word):
        temp = []
        for i in range(len(word)):
            if i == 0:
                temp.append(word[len(word)-1])
            else:
                temp.append(word[i-1])
        temp = ''.join(temp)
        return temp
    l1 = list(a)
    l2 = list(b)
    for i in range(len(l2)):
        if l1.count(l2[i]) != 0:
            return True
        l2 = rotate_word(l2)
    return False







