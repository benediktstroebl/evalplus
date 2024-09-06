
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            for k in range(j+1, len(a)):
                for l in range(k+1, len(a)):
                    pattern = b[i:j+1] + b[j+1:k+1] + b[k+1:l+1] + b[l+1:]
                    if a[i:j+1] in b or b[j+1:k+1] in b or b[k+1:l+1] in b or b[l+1:] in a:
                        return True
    return False