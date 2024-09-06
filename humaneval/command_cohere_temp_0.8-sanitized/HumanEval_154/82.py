def cycpattern_check(first, second):
    """
    You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word.
    """
    first = first.lower()
    second = second.lower()
    
    # Check if the second word is a substring of the first word
    if second in first:
        return True
    
    # Check for rotations of the second word
    second = second[1:] + second[:1]
    return any(rot in first for rot in second.split())