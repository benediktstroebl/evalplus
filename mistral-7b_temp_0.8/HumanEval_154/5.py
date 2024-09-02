
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    a=a.lower()
    b=b.lower()
    a_list=list(a)
    b_list=list(b)
    # print(b_list)
    if len(a_list)==len(b_list):
        for i in range(len(b_list)):
            for j in range(len(b_list)):
                if b_list[i]!=b_list[j]:
                    return False
        return True
    else:
        return False
    # print(a_list)

