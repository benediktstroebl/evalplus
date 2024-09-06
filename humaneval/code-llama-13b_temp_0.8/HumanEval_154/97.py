
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    check_list = [a]
    temp = a
    for i in range(len(a)-1):
        temp = temp[-1] + temp[0:len(a)-1]
        check_list.append(temp)

    if b in check_list:
        return True
    else:
        return False
