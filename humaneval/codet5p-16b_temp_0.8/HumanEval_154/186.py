
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """

    a_index = 0
    for i in range(len(a)):
        if a[a_index]!= a[i]:
            a_index += 1
            a[a_index] = a[i]
    a_index += 1
    a_index %= len(a)

    b_index = 0
    for i in range(len(b)):
        if a[b_index]!= b[i]:
            b_index += 1
            b[b_index] = b[i]
    b_index += 1
    b_index %= len(b)

    if a_index < len(a) and b_index < len(b):
        return True
    return False

