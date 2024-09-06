
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    _a = a + a
    _b = b + b
    if b in _a and len(b) > len(a):
        return True
    if len(b) == len(a):
        return False
    for i in range(len(a)):
        if b in _a[i:len(a)+i]:
            return True
    return False

tests = [
    (("abcd", "abd"), False),
    (("hello", "ell"), True),
    (("whassup", "psus"), False),
    (("abab", "baa"), True),
    (("efef", "eeff"), False),
    (("himenss", "simen"), True),
    (("ababc", "baabc"), True),
    (("abcde", "bcdea"), True),
    (("aaaaa", "aaabb"), True),
    (("qwerty", "wefgh"), False)
]


for test, expected in tests:
    assert cycpattern_check(*test) == expected
