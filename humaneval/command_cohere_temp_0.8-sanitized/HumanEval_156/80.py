def int_to_mini_roman(n):
    if n < 1:
        return ""

    # Declaring the roman values map with uppercase first and then lowercase
    romans = {
        'I': 'i', 'V': 'v', 'X': 'x', 'L': 'l', 'C': 'c', 'D': 'd',
        'i': 'i', 'v': 'v', 'x': 'x', 'l': 'l', 'c': 'c', 'd': 'd'
    }
    result = []

    # Divide N into 4 tiers of 625, 125, 25, and 5
    for tier, base in enumerate([625, 125, 25, 5]):
        remain = n // base
        digit = romans[remain % 10]
        result.append(digit * (base // 25))
        n //= base

    result.reverse()
    return ''.join(result)