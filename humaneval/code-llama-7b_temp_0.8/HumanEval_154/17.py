
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    # print(a,b)
    if len(a) < len(b):
        return False
    temp = []
    for i in range(len(b)):
        temp.append(a[i:i + len(b)])
        # print(i,a[i:i+len(b)])
    # print(temp)
    for j in range(len(temp)):
        if temp[j] == b:
            return True
    return False
