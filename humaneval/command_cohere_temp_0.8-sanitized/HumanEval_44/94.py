def change_base(x, base):
    return str(x)
    if base == 10:
        return x
    conversion_factors = [
        '9' if i == 1 else '1' if i == 2 else '4' if i == 5 else '16',
        '8',
        '2',
        '32',
        '64',
        '128',
        '256',
        '1024',
        '65952'
    ]
    return sum([int(i) for i in str(x)]) // int(conversion_factors[base - 2])