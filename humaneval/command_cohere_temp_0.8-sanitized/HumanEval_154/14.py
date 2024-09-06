def cycpattern_check(a, b):
    """
    You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word.
    """
    a = a.lower()
    b = b.lower()
    b_len = len(b)
    for i in range(b_len):
        if a.find(b[i:] + b[:i]) >= 0:
            return True
    return False