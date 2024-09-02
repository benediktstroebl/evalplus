
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    from string import punctuation
    from string import ascii_letters
    def rotate_word(word):
        """Rotates the word by shifting characters along"""
        return ''.join(sorted(word))

    a_rotated = rotate_word(a)
    b_rotated = rotate_word(b)

    for b_sub in set(b_rotated.split()):
        if b_sub in a_rotated:
            return True

    for b_rot in [rotate_word(b_rotated) for b_rot in set(b_rotated)]:
        if any(b_rot in a for a in set(a_rotated.split())):
            return True

    return False
