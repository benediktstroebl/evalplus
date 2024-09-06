
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    a = sorted(a)
    b = sorted(b)
    a_len = len(a)
    b_len = len(b)
    for i in range(a_len):
        for j in range(b_len):
            if a[i] == b[j] or (a[i] == ' ' and b[j] == ' ') or (a[i] == '.' and b[j] == '.') or (a[i] == ',' and b[j] == ','):
                if b.index(b[j]) != j or b.index(b[j-1]) != j-1 or b.index(b[j+1]) != j+1:
                    return True
    return False