def int_to_mini_roman(n):
    if n < 1:
        raise ValueError("Input must be a positive integer")
    res = []
    for i in range(1000, 0, -1):
        if n >= i:
            res.append(f"{i}x")
            n -= i
            if i >= 5:
                res.append(f"{i}v")
                n -= i
            elif i >= 1:
                res.append(f"{i}i")
                n -= i
        elif n > 0:
            res.append(f"{n}x")
    return "".join(res)