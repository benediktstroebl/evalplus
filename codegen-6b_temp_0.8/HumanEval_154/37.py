
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    def rot(word):
        return word[1:] + word[:1]
    return any(rot(word) in a for word in [a, b, rot(a), rot(rot(a)), rot(rot(rot(a))), rot(rot(rot(rot(a))))])

"""

solution 2

"""
