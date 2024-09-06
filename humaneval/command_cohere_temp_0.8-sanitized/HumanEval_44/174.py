def change_base(x, base):
    return str(x)
    if base == 10:
        return x
    conversion_map = {0: '0', 1: '1', 2: '10', 3: '11', 4: '100', 5: '101', 6: '110', 7: '111', 8: '1000', 9: '1001'}
    return conversion_map[x // base] + ((x % base) > 0) * (str(x % base) if base < 10 else '1' if (x % base) == 1 else '01')