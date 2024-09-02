
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    max_len = max(len(word) for word in [a,b])
    for i in range(max_len+1):
        for word in [a,b]:
            word_rot = word + "o"*(max_len-len(word))
            if word in word_rot:
                return True
    return False
