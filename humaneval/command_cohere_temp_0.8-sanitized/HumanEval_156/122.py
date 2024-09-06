def int_to_mini_roman(n):
    if n < 1:
        raise ValueError("Input must be a positive integer")
    res = []
    for i in range(1000):
        if n >= i:
            num = [str(j) for j in reversed(list(range(i, i + 1)))]
            res += [next(d for d in num if d != '0')]
            n -= i
    return ''.join(res)