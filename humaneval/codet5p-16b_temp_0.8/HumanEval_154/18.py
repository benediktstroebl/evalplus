
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """

    a_list = list(a)
    b_list = list(b)
    
    len_a = len(a_list)
    len_b = len(b_list)

    for i in range(len_b):
        if b_list[i:] + b_list[:i] == a_list or b_list[i:] + b_list[:i] == a_list[::-1] or b_list[i:] + b_list[:i] == a_list[len_a-i:] + a_list[:len_a-i]:
            return True
    return False

