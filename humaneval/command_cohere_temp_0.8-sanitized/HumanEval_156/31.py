def int_to_mini_roman(n):
    if n < 1:
        raise ValueError("Input must be a positive integer")
    res = []
    for i in range(1, 1000):
        if n >= i:
            num = [str(i) for i in range(1, (i//5)+1)]
            den = [str(i) for i in range(1, (i//10)+1)]
            res += [den[0]+num[0]+(len(num)>=2 and den[1] or '')+str(i//10*5)]
            n -= i
    return ''.join(res)