def int_to_mini_roman(n):
    if n < 1:
        raise ValueError("Input must be a positive integer")
    res = []
    for i in range(1, 1000):
        if n >= i:
            count = len(str(i))
            res.extend(str(i)[::-1][:count])
            n -= i
    return ''.join(res)