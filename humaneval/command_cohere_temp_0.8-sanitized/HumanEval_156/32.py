def int_to_mini_roman(num):
    if num < 1000:
        converter = [
            lambda x: 'i' if x == 1 else 'iv' if x == 4 else 'v' if x == 5 else 'ix',
            lambda x: 'v' if x == 5 else 'x' if x == 10 else 'l' if x == 50 else 'c',
            lambda x: 'i' if x == 1 else 'v' if x == 5 else 'x' if x == 10 else 'l' if x == 50 else 'c',
            lambda x: 'i' if x == 1 else 'iv' if x == 4 else 'v' if x == 5 else 'ix' if x == 9 else 'x',
            lambda x: 'v' if x == 5 else 'x' if x == 10 else 'l' if x == 50 else 'c',
            lambda x: 'i' if x == 1 else 'v' if x == 5 else 'xx' if x == 10 else 'l' if x == 50 else 'c',
            lambda x: 'i' if x == 1 else 'iv' if x == 4 else 'v' if x == 5 else 'ix' if x == 9 else 'xx',
            lambda x: 'v' if x == 5 else 'xx' if x == 10 else 'l' if x == 50 else 'c',
            lambda x: 'i' if x == 1 else 'v' if x == 5 else 'xxx' if x == 10 else 'l' if x == 50 else 'c',
            lambda x: 'v' if x == 5 else 'xxx' if x == 10 else 'l' if x == 50 else 'c',
            lambda x: 'v' if x == 5 else 'xxxx' if x == 10 else 'l' if x == 50 else 'c',
        ][num // 100]
        num = num % 100
    return converter(num)