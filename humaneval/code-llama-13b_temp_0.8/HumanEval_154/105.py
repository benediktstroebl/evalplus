
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if len(a)<len(b):
        return False

    if len(a)==len(b):
        return True if a==b else False
    b_list = list(b)
    b_list.sort()
    b_list = ''.join(b_list)

    for i in range(0,len(a)-len(b)+1):
        a_slice = a[i:i+len(b)]
        a_list = list(a_slice)
        a_list.sort()
        a_list = ''.join(a_list)
        if a_list==b_list:
            return True

    return False



