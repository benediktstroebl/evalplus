def cycpattern_check(first, second):
    """
    You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word.
    """
    first = first.lower()
    second = second.lower()
    rotated_seconds = [second[i:] + second[:i] for i in range(len(second))]
    return any(second in first or rotated_second in first for rotated_second in rotated_seconds)