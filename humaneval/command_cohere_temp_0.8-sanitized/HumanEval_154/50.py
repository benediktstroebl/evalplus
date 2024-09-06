def cycpattern_check(first, second):
    return second in set(map(lambda x: x[:len(second)] , (s[:i] for i in range(len(s) + 1) for s in (first, second)) ))