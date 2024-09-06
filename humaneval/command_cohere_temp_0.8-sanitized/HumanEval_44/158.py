def change_base(x, base):
    return str(x)
    if base == 10:
        return x
    conversion_map = {0: '0', 1: '1', 2: '2', 3: '10', 4: '11', 
                       5: '12', 6: '13', 7: '14', 8: '15', 9: '16'}
    result = 0
    while x > 0:
        remainder = x % base
        x = x // base
        result = result * 10 + conversion_map[remainder]
    return result