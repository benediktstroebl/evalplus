def cycpattern_check(first, second):
    return second in set(map(lambda x: x[:len(second)] , (s[:i] for s in itertools.permutations(first, len(first)) for i in range(len(first)))))