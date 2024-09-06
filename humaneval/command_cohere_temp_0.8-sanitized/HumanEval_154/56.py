def cycpattern_check(first, second):
    """
    You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word.
    """
    first = first.lower()
    second = second.lower()
    
    return second in first or any(x for x in first if x == second)