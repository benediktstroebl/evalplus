def int_to_mini_roman(n):
    if n < 1:
        return ""
    
    res = []
    for i in range(1, 1000):
        if n >= i:
            num = [str(d) for d in reversed(list(range(i, i + 1)))]
            res.extend(num)
            n -= i
            if n == 0:
                break
    return ''.join(res).lower()