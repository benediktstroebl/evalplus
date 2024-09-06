
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    def gen_cycle_tarr(a, b):
        n = len(a)
        t = [[False]*n for i in range(n)]
        for i in range(n):
            t[i][i] = True
        for j in range(1, n):
            for i in range(n-j):
                if a[i] == a[i + j] and t[i + 1][i+j-1]:
                    t[i][i+j] = True
        return t
    t = gen_cycle_tarr(a, b)
    return any(t[0][j-1] for j in range(1, len(b) + 1))

