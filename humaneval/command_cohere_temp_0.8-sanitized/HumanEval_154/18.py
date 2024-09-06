def cycpattern_check(first, second):
    return second in set(map(lambda x: x[:len(second)] , (iter(first.split()))))