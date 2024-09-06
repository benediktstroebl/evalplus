
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """

    # We'll use a set to store our pattern
    pattern = set(b)

    # we'll use a sliding window
    # It will be of size len(pattern)
    for i in range(len(a) - len(b) + 1):
        if pattern.issubset(set(a[i:i+len(b)])):
            return True
    return False


