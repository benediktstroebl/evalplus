def int_to_mini_roman(n):
    if n < 1:
        raise ValueError("Input must be a positive integer")
    res = []
    for i in range(1, 1000):
        if n >= i:
            num = [str(j) for j in range(i, 0, -1)]
            mini_roman = ''
            for j in range(len(num)):
                mini_roman += num[j]
            res.append(mini_roman)
            n -= i
    if n != 0:
        res.append(str(n))
    return ''.join(res)