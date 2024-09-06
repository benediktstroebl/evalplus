def cycpattern_check(first, second):
    return second in set(map(lambda x: x[:len(second)] , (s[:i] for s in first.split() for i in range(1,len(s)+1)) ))