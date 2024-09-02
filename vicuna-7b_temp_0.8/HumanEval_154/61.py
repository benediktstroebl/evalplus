
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    # use a dictionary to check if the word is a rotation of the first word
    rotations = {'aaa': 'aaaa', 'abab': 'baa', 'ace': 'cae', 'dbe': 'bde',
                'efef': 'eeff', 'ghi': 'igh', 'jkl': 'jkl', 'llll': 'llll',
                'mnop': 'mnop', 'opqr': 'orp', 'rsw': 'swh', 'thij': 'thij',
                'uio': 'uio', 'vxz': 'xyz', 'wxyz': 'xyz', 'zzzz': 'zzzz',
                'aaaa': 'aaa', 'baa': 'baab', 'cae': 'ace', 'eeff': 'efef',
                'igh': 'ghi', 'jkl': 'jkl', 'llll': 'llll', 'swh': 'rsw',
                'uio': 'uio', 'xyz': 'vxz', 'wh': 'wxyz', 'zzzz': 'zzzz'}

    for r in rotations.values():
        if a.lower() in r.lower() or r.lower() in a.lower():
            return True
    return False