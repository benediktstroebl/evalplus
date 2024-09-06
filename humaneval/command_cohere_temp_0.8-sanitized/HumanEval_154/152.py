def cycpattern_check(first, second):
    first = first.lower()
    second = second.lower()
    return second in first or any(second in t for t in first.split(second))