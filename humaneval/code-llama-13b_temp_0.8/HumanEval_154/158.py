
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if not(a and b):
        return False

    if len(a) != len(b):
        return False

    if b not in a:
        return False

    s_list = []
    s = b
    for i in range(len(s)-1):
        s = s[1:] + s[0]
        s_list.append(s)

    if any([x in s_list for x in a]):
        return True
    else:
        return False
