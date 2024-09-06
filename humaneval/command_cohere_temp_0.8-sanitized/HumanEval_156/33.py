def int_to_mini_roman(n):
    if n < 1:
        raise ValueError("Input must be a positive integer")

    res = []
    for i in range(1000, 0, -1):
        if n >= i:
            res.append(str(i))
            n -= i
            if i >= 5 and n > 0:
                res.append('x')
                n -= 1
        elif n > 0:
            res.append('x')
            n -= 1

    return ''.join(res)