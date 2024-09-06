
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
        for j in range(len(b)):
            if a[i+j]==b[j]:
                x=i+j
                y=j
                while(x<len(a) and y<len(b)):
                    if a[x]!=b[y]:
                        break
                    x=x+1
                    y=y+1
                else:
                    return True
    return False

