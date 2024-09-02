
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    x = len(a)
    #print(x)
    y = len(b)
    #print(y)
    result = []
    for i in range(y):
        if a.find(b) != -1:
            #print(a.find(b))
            return True
        else:
            if b.find(b[-1]) == -1:
                return False
            else:
                b = b[1:] + b[0]
                #print(b)
                #print(b[-1])
    #print(b)


