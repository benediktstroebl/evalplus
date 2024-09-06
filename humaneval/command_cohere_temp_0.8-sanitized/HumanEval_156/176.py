def int_to_mini_roman(n):
    if n < 1:
        raise ValueError("Input must be a positive integer")
    res = []
    for i in range(1, 1000):
        if n >= i:
            res += [str(i) if i not in ['i', 'iv', 'ix', 'xl'] else 'ii' for i in range(1, i + 1)]
            n -= i
            if n > 0:
                res.append('x')
    return ''.join(res)