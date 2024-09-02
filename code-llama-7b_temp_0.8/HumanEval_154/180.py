
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    def rotate(a, i):
        """
        takes a string a and returns the string a rotated by i positions to the left
        >>> rotate('abcde', 2)
        'cdeab'
        >>> rotate('abcde', 0)
        'abcde'
        >>> rotate('abcde', 5)
        'abcde'
        """
        return a[i:] + a[:i]

    for i in range(len(b)):
        if b in a:
            return True
        elif rotate(a, i) == b:
            return True
    return False

