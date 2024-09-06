def cycpattern_check(first, second):
    first = first.lower()
    second = second.lower()
    return second in first or any(x in first for x in second[::-1])