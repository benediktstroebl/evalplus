
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """

    def rotate(word):
        return word[1:] + word[0]

    def is_substring(s, w):
        return s.find(w) != -1

    return is_substring(a, b) or any(is_substring(rotate(a), b) for i in range(len(b)))

    # if b in a:
    #     return True
    # return any(rotate(a, i).find(b) != -1 for i in range(len(b)))

