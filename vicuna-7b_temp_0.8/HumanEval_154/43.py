
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if len(a)<len(b):
        return False
    for i in range(len(b)-1):
        if b[i:i+len(a)] in a:
            return True
    return False

lst = [["abab","baa"],["efef","eeff"],["hello","ell"],["whassup","psus"],["abcd","abd"]]
for i in range(len(lst)):
    a = lst[i][0]
    b = lst[i][1]
    if cycpattern_check(a,b):
        print(i+1,a,b)