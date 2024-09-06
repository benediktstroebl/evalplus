
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    x,y = a,b
    x = x.upper()
    y = y.upper()
    for i in range(len(x)):
        for j in range(len(y)):
            if y[j] == x[i] and x[i] in y[j+1:]:
                return True
    return False

a = input().lower()
b = input().lower()
