
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    #print(a,b)
    #print(len(a),len(b))
    if len(a) < len(b):
        return False
    if len(a) == len(b):
        for i in range(len(a)):
            if a == b:
                return True
            a = a[1:] + a[0]
    if len(b) % len(a) == 0:
        for i in range(len(b)//len(a)):
            for j in range(i,len(b),len(a)):
                #print(a,b,j,j+len(a))
                if a == b[j:j+len(a)]:
                    return True
                #a = a[1:] + a[0]
    return False

