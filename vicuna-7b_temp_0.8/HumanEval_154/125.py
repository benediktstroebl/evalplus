
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if len(a) < len(b):
        return False
    a_rotated = ""
    for char in a:
        a_rotated += char.upper()
    b_rotated = ""
    for char in b:
        b_rotated += char.upper()
    for i in range(len(a_rotated) + 1):
        if a_rotated[i:i+len(b)] in a or a_rotated[i:i+len(b)] == b or a_rotated[i:i+len(b)] == b[::-1]:
            return True
    return False