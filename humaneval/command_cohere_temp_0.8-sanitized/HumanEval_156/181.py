def int_to_mini_roman(n):
    if n < 1:
        return ""
    
    res = []
    for i in range(1, 1000):
        if n >= i:
            res += [str(i) for i in range(1, len(str(i)) + 1) if str(i)[len(str(i)) - i + 1]!='0']
            n -= i

    return ''.join(res)