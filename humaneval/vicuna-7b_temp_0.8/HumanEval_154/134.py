
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    #your code here
    a_lower = a.lower()
    b_lower = b.lower()
    b_rot = [word for word in b_lower.split() if word != b_lower[0]]
    for b_rot_word in b_rot:
        if a_lower.find(b_rot_word) != -1 or a_lower.find(b_rot_word.lower()) != -1:
            return True
    return False
