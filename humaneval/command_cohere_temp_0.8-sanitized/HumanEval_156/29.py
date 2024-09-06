def int_to_mini_roman(num):
    converter = [
        [1000, 'm'],
        [900, 'cm'],
        [500, 'd'],
        [400, 'cd'],
        [100, 'c'],
        [90, 'xc'],
        [50, 'l'],
        [40, 'xl'],
        [10, 'x'],
        [9, 'ix'],
        [5, 'v'],
        [4, 'iv'],
        [1, 'i']
    ]
    roman = []
    for dim in converter:
        for idx in range(num // dim[0]):
            roman.append(dim[1])
        num %= dim[0]
    return ''.join(roman).lower()