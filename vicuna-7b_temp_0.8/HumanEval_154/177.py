
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    n = len(a)
    for i in range(n):
        for j in range(i+1, n):
            if a[i:j] in b:
                if any(b.find(x) != -1 for x in rotate(a[i:j])) or any(b.find(x) != -1 for x in rotate(a[j:i])):
                    return True
    return False