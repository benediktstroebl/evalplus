
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    # print(a)
    # print(b)
    for x in b.split():
        # print(x)
        for i in range(len(a)):
            for j in range(i+1,len(a)):
                for k in range(j+1,len(a)):
                    for l in range(k+1,len(a)):
                        if b[i:j+1] in a[j:l+1] or b[i:k+1] in a[l:k+1] or b[i:l+1] in a[k:j+1] or b[i:k+1] in a[j:l+1]:
                            return True
    return False
