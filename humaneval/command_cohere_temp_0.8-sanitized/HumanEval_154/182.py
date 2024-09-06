def cycpattern_check(a, b):
    """
    You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word.
    """
    a = a.lower()
    b = b.lower()
    b = b.replace(" ","")
    b = b.strip(".")
    b = b.strip("!")
    b = b.strip("?")
    rotations = [b[i:]+b[:i] for i in range(len(b)/2)]
    return any(rot in a for rot in rotations)