def cycpattern_check(a, b):
    """
    You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word.
    """
    a = a.lower()
    b = b.lower()
    b = b.replace("{}".format(a[0]), "")
    return (
        b in a
        or a.startswith(b)
        or a.endswith(b)
        or cycpattern_check(a[1:], b)
        or cycpattern_check(a[:-1], b)
    )