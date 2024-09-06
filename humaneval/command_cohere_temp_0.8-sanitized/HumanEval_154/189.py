def cycpattern_check(first, second):
    return second in set(rotated(second) for rotated in (x[:i] + x[i:] for i in range(len(x) // 2)))
def rotated(string):
    return [string[i:] + string[:i] for i in range(len(string))]