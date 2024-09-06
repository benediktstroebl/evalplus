def int_to_mini_roman(n):
    if n < 1:
        return ""
    
    res = []
    for i in range(1, 1000):
        if n >= i:
            num = [str(j) for j in range(i, 0, -1)]
            res.extend(num)
            n -= i
    
    return ''.join(res)