
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """

    def rotate_word(a,n):
        output = ""
        for i in range(len(a)):
            output += a[i-n]
        return output

    for i in range(1,len(a)+1):
        if b in a or b in rotate_word(a,i):
            return True
    return False

