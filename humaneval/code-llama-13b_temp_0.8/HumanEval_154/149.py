
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    # your code goes here
    x = len(a)
    y = len(b)
    for i in range(0,x):
        for j in range(0,y):
            if(a[i:x] == b[j:y]):
                return True
            else:
                if(j == y-1):
                    b = b[::-1]
                    j = 0
                    y = len(b)
                else:
                    j = j + 1
    return False

