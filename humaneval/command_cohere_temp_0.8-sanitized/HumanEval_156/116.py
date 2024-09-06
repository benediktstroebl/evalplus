def int_to_mini_roman(n):
    if n < 1:
        return ""

    res = []
    for i in range(1, 1000):
        if n >= i:
            res += [c for c in f"{{:,}}".format(i) if c != '0']
            n -= i

    return ''.join(res)