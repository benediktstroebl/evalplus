
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    from string import ascii_uppercase
    from typing import List

    b_rotated = [chr(i + ord('a') + j) for j in range(len(b)) for i in range(len(a))]
    b_rotated_check = [b[::-1] for b in b_rotated]

    for r in b_rotated_check:
        if r in a:
            return True
    return False