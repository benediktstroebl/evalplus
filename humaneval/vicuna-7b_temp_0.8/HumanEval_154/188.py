
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if len(a) != len(b):
        return False

    c = ""
    for i in range(len(a)):
        c += a[i]
        for j in range(len(b)):
            if b[j] == c[len(c)-1]:
                if b[j+1:j+len(b)-j-1] in a:
                    return True
                break
        c = b[j]
    return False

b = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]

for i in range(len(b)):
    for j in range(len(b[0])):
        if b[i][j] == b[i][j+1]:
            print("1")