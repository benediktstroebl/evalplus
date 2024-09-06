def cycpattern_check(a, b):
    """
    You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word.
    """
    a = a + a
    b = b + b
    return any(b in a for _ in range(len(b)))