def int_to_mini_roman(n):
    if n < 1:
        raise ValueError("Input must be a positive integer")
    res = []
    for i in range(1, 1000):
        if n >= i:
            count = len(str(i))
            res.extend([str(j) for j in range(count)])
            n -= i
            if n == 0:
                break
    return ''.join(res).lower()