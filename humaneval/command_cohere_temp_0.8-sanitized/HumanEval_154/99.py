def cycpattern_check(first, second):
    """
    You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word.
    """
    first = first.lower()
    second = second.lower()
    rotations = [second, second[1:] + second[:1], second[2:] + second[:2], second[3:] + second[:3]]
    return any(rotations) in first