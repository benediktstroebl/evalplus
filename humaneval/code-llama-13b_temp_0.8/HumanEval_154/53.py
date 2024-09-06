
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    def substring(word1 , word2):
        n = len(word1)
        m = len(word2)
        for i in range(n-m+1):
            for j in range(m):
                if word1[i+j]!=word2[j]:
                    break
            if j==m-1:
                return True
        return False
    def rotate(word):
        n = len(word)
        for i in range(n):
            yield word[n-1:] + word[:n-1]
    for i in rotate(b):
        if substring(a, i):
            return True
    return False
