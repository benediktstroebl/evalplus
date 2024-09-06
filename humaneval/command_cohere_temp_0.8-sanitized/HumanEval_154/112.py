def cycpattern_check(first, second):
    return second in set(map(lambda x: x[:len(second)] , (iter(first.upper()) if len(first) > len(second) else iter(first))))